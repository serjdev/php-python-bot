import vk, os, json, time
from threading import Thread
from requests import post
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')

TOKEN = config.get('vk', 'token')
API = config.get('vk', 'v')
BOT_ID = config.get('vk', 'group_id')

time = time.time()
session = vk.Session(access_token = TOKEN)
vk = vk.API(session, v = API)

long_poll = vk.groups.getLongPollServer(group_id = BOT_ID)
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']

def addslashes(s):
	return repr('"' + s)[2:-1].replace('"', '\\"')

while True:
	try:
		long_poll = post('%s'%server, data = {'act': 'a_check', 'key': key, 'ts': ts,  'wait': 90}).json()
	except Exception:
		quit();
	updates = long_poll['updates']
	if updates is None:
		long_poll = vk.groups.getLongPollServer(group_id = BOT_ID)
		server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
		if server == null:
			quit()
		continue
	if long_poll['updates'] and len(long_poll['updates']) != 0:
		for up in long_poll['updates']:
			if ((up['type'] == 'message_new') and up['object']['message']['from_id'] > 0):
				print(os.system('php ./src/bot.php "'+addslashes(json.dumps(up['object']))+'" &'))

	ts = long_poll['ts']
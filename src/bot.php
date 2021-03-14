<?php

# Start
(new Bot($argv[1]));

class bot {
    public array $updates;
    public int|float $peer_id, $user_id;
    public string $message;

    public function __construct(string $updates) {
        $this->updates = json_decode($updates, true);
        $this->peer_id = $this->updates['message']['peer_id'];
        $this->user_id = $this->updates['message']['from_id'];
        $this->message = $this->updates['message']['text'];
        $this->checkCommands();
    }

    public function checkCommands() : void {
        if ($this->message == "Привет") {
            self::call("messages.send", [
                "random_id" => rand(),
                "message" => "Привет, я бот!",
                "peer_id" => $this->peer_id
            ]);
        }
    }

    public static function call(string $method, array $params) : array {
        $config = parse_ini_file("./config.ini");
        $params['access_token'] = $config['token'];
        $params['v'] = $config['v'];
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://api.vk.com/method/' . $method);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($params));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $curl_result = curl_exec($ch);
        curl_close($ch);
        return json_decode($curl_result, true);
    }
}
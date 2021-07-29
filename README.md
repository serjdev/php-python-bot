![alt text](https://serjdev.ru.com/php-py.png)


[![Latest Stable Version](https://poser.pugx.org/serjdev/php-python-bot/v)](//packagist.org/packages/serjdev/php-python-bot) [![Total Downloads](https://poser.pugx.org/serjdev/php-python-bot/downloads)](//packagist.org/packages/serjdev/php-python-bot) [![Latest Unstable Version](https://poser.pugx.org/serjdev/php-python-bot/v/unstable)](//packagist.org/packages/serjdev/php-python-bot) [![License](https://poser.pugx.org/serjdev/php-python-bot/license)](//packagist.org/packages/serjdev/php-python-bot)

# Установка скрипта
```shell
$ git clone https://github.com/frogserj/php-python-bot
```

# Установка зависимостей
```shell
$ pip3 install vk
```

# Тестовая команда
```php
public function checkCommands() : void {
        if ($this->message == "Привет") {
            self::call("messages.send", [
                "random_id" => rand(),
                "message" => "Привет, я бот!",
                "peer_id" => $this->peer_id
            ]);
        }
    }
```

# Настройка `config.ini`
```ini
[vk]
token = access_token # Токен группы
group_id = 123 # ID группы
v = 5.130 # Версия API ВКонтакте
```

# Выдача прав и запуск скрипта
```shell
$ chmod +x start.sh
$ ./start.sh
```

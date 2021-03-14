### Многопоточность PHP / Python

<p align="center">
    <a href="https://packagist.org/packages/serjdev/php-python-bot"><img alt="Total Downloads" src="https://poser.pugx.org/serjdev/php-python-bot/downloads"></a>
    <a href="https://packagist.org/packages/serjdev/php-python-bot"><img alt="Latest Stable Version" src="https://poser.pugx.org/serjdev/php-python-bot/v/stable"></a>
    <a href="https://packagist.org/packages/serjdev/php-python-bot"><img alt="License" src="https://poser.pugx.org/serjdev/php-python-bot/license"></a>
</p>

# Установка скрипта
```shell
$ git clone https://github.com/serjdev/php-python-bot
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

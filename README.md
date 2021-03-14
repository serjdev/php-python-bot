### Многопоточность PHP / Python

# Установка скрипта
```shell
git clone https://github.com/serjdev/php-python-bot
```

# Установка зависимостей
```shell
pip3 install vk
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
chmod +x start.sh
./start.sh
```

# python-weather-auth-service
Сервис для авторизации на gRPC. Возвращает `true` если имя полученного пользователя есть в хеш-таблице, иначе возвращает `false`

## Запуск
```
python server.py
```

## Данные

Приходит
```
message RequestAuth {
    string name = 1;
}

```

Возвращается
```
message ResponseAuth {
    bool isAuth = 1;
}
```

## Тест
Запуск тестового клиента

```
python testClient.py
```
Изменив параметр `name` в функции `RequestAuth`, будет меняться запрос

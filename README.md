# python-weather-auth-service
Сервис для авторизации на gRPC. Возвращает `true` если имя полученного пользователя есть в хеш-таблице, иначе возвращает `false`

## Запуск
```
python server.py
```

## Данные

Получает
```
message RequestAuth {
    string name = 1;
}

```

Отправляет
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

## Docker
Auth сервис интегрирован с [сервисом погоды](https://github.com/SerBEEan/express-weather-api "express-weather-api") через `docker-compose`.
Поэтому, при необходимости запустить отдельно, расширьте `Dockerfile` для вывода портов:

```
EXPOSE 8080
```

Соберите образ и запустите контейнер

```
docker build -t auth .
```
```
docker run -p 8080:8080 auth
```

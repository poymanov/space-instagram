# Публикация фотографий из космоса в Instagram

Приложение получает фотографии космоса
через [SpaceX API](https://github.com/r-spacex/SpaceX-API), [Hubble API](http://hubblesite.org/api/documentation)
и загружает их в пользовательский аккаунт [Instagram](https://www.instagram.com).

### Как установить

Установить **docker** и **docker-compose**

Выполнить:
```
make
```

Заполнить необходимые параметры в `.env`:
```
IMAGES_PATH - путь к директории для хранения загруженных изображений (создается автоматически)
INSTAGRAM_USERNAME - логин пользователя в Instagram
INSTAGRAM_PASSWORD - пароль пользователя в Instagram
```

Запуск:
```
make run
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

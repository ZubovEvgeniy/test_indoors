
# Cats blog

Сервис для заводчиков котов с возможностью общения и публикации карточек о своих любимцах, просмотра кошек других заводчиков и редактирования своих карточек.


## Запуск проекта

### Запуск локально на Windows

1. Клонировать проект из репозитория GitHub:
```
  git clone git@github.com:ZubovEvgeniy/test_indoors.git
```

2. Установить виртуальное окружение
```
  python -m venv venv
```

3. Активировать виртуальное окружение
```
  source venv/Scripts/activate
```

4. Обновить pip
```
  python -m pip install --upgrade pip
```

5. Установить зависимости
```
  cd cats_blog
```
```
  pip install -r requirements.txt
```

6. Запустить проект
```
  python manage.py runserver
```
Чат доступен на главной странице http://127.0.0.1:8000/

### Запуск из образа Docker Compose*

1. Клонировать проект из репозитория GitHub:
```
  git clone git@github.com:ZubovEvgeniy/test_indoors.git
```

2. Собрать контейнеры
```
  cd cats_blog
```
```
  docker-compose up -d --build
```
3. Применить миграции
```
  docker-compose exec web python manage.py migrate
```
4. Собрать статические файлы
```
  docker-compose exec web python manage.py collectstatic --no-input
```
Проект доступен по адресу http://localhost/

**- при запуске через docker функция чата не реализована (пока)*


## API Reference 



#### Request

Для взаимодействия с сервисом отправьте запросы:

```
POST /auth/users/
```
Зарегистрировать нового пользователя

В теле запроса передать `username` и `password`

```
POST /auth/jwt/create/
```
Получить токен пользователя

В теле запроса передать `username` и `password`

```
GET blog/cats/<int:pk>/
```
Получить карточку одного кота

Доступно только хозяину кота

Response:
```
{
    "name": "Mysya",
    "color": "Ginger",
    "birth_year": 2018,
    "age": 5,
    "breed": "dvorovaya",
    "owner": "Ivan_Petrov"
}
```

```
POST blog/cats/
```
Опубликовать карточку своего кота

В теле запроса передать `name`, `color`, `birth_year`, `breed`

```
GET /blog/cats/
```
Получить список всех котов

```
PUTCH /blog/cats/<int:pk>/
```
Изменить поле в карточке кота

Доступно только хозяину кота

```
DELETE /blog/cats/<int:pk>/
```
Удалить карточку кота

Доступно только хозяину кота

```
GET /blog/owners/<int:pk>/
```
Посмотреть карточку одного заводчика

Response:
```
{
    "username": "Petr_Ivanov",
    "cats": [
        "Myrzik",
        "Vasya"
    ]
}
```

```
GET /blog/owners/
```
Посмотреть список всех заводчиков


## Технологии

* Python 3.9
* Django 4
* DRF 3.14
* SimpleJWT
* Djoser
* Docker 


## Authors

- [Зубов Евгений](https://github.com/ZubovEvgeniy)


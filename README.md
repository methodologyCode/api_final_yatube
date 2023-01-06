# API для социальной сети

## Описание:

API для социальной сети, в которой можно публиковать собственные записи и подписываться на других авторов.

Запустить проект можно следующим образом:

- Склонировать Репозиторий:

```
https://github.com/methodologyCode/api_final_yatube
```

```
cd api_final_yatube
```

- Cоздайте и активируйте виртуальное окружение:

Linux:
```
python3 -m venv venv
```

Windows:

```
python -m venv venv
```

затем:

Linux:
```
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate либо .\venv\Scripts\activate
```


- Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

- Выполните миграции:

```
python manage.py migrate
```

Запустите проект:

```
python manage.py runserver
```

Документация:

http://127.0.0.1:8000/redoc/

Примеры запросов:

```
Получение всех постов

http://127.0.0.1:8000/api/v1/posts/
```

```
Получение комментариев

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

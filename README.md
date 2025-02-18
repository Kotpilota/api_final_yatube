# API для Yatube

**Описание:**  
Проект представляет собой REST‑API для социальной сети Yatube. API позволяет получать и создавать публикации, комментарии, подписки и работать с сообществами. Для аутентификации используются JWT‑токены.

**Установка:**  
1. Клонируйте репозиторий:  
```bash
git clone https://github.com/Kotpilota/api_final_yatube.git
```

2. Перейдите в папку проекта и создайте виртуальное окружение: 
```bash
python -m venv venv
```
Linux/MacOS
```bash
source venv/bin/activate 
```
Windows
```bash
venv\Scripts\activate
```

3. Установите зависимости:  
```bash
pip install -r requirements.txt
```

4. Выполните миграции:  
```bash
cd yatube_api
```
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Запустите сервер:  
```bash
python manage.py runserver 
```

---

**Примеры запросов к API:**  
- Получить список публикаций: 
```
GET http://127.0.0.1:8000/api/v1/posts/
```

- Получить JWT‑токен:
```
POST http://127.0.0.1:8000/api/v1/jwt/create/ { "username": "your_username", "password": "your_password" }
```

- Создать публикацию (требуется JWT‑токен):  
```
POST http://127.0.0.1:8000/api/v1/posts/ { "text": "Новая публикация", "group": 1 }
```


- Подписаться на пользователя (требуется JWT‑токен): 
```
POST http://127.0.0.1:8000/api/v1/follow/ { "following": "username_target" }
```

Документация доступна по адресу: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Для того щоб запустити проект потрібно:

1. створити віртуальне середовище:
python3 -m venv venv
source venv/bin/activate
2. Встанови залежності:
pip install -r requirements.txt
3. Необовʼявзково, але налаштувати середовище
export EMAIL_USER=твоя_пошта@gmail.com
export EMAIL_PASS=пароль_або_app_password
export SECRET_KEY=будь_який_рядок
4. Якщо немає створенох БД, то створити:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Запустити проект через main.py
python3 main.py

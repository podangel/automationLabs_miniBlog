Для того щоб запустити проект потрібно:

1. зібрати проект: make install
2. якщо немає БД створити: make init_DB
3. запустити проект: make run



deprecated:
створити віртуальне середовище: 
python3 -m venv venv 
source venv/bin/activate

Встанови залежності: 
pip install -r requirements.txt

Необовʼявзково, але налаштувати середовище:
export EMAIL_USER=твоя_пошта@gmail.com 
export EMAIL_PASS=пароль_або_app_password 
export SECRET_KEY=будь_який_рядок

Якщо немає створенох БД, то створити:
flask db init 
flask db migrate -m "Initial migration" 
flask db upgrade

Запустити проект через main.py 
python3 main.py
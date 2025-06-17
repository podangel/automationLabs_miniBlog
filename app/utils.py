from flask import url_for, current_app
from flask_mail import Message
from app import mail

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Скидання пароля',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''Щоб скинути пароль, перейдіть за посиланням:
{url_for('main.reset_token', token=token, _external=True)}

Якщо ви не робили цей запит, просто ігноруйте це повідомлення.
'''
    mail.send(msg)

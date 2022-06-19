from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db, User

app = create_app()

with app.app_context():
    username = input('Введите имя: ')

    if User.query.filter(User.username == username).count():
        print('Пользователь с таким именем уже существует')
        sys.exit()

    password1 = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')

    if not password1 == password2:
        print('Пароли не сопадают')
        sys.exit()

    new_user = User()
    new_user.username = username
    new_user.role = 'user'
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Создан пользователь {new_user.username} с {new_user.id=}')

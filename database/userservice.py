from database.models import User
from database import get_db
from datetime import datetime


# регистрация
def registration_user_db(name, surname, email, phone_number, country, password, reg_date):
    db = next(get_db())

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number, country=country, password=password, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return f'Пользователь {name} успешно прошёл регистрацию'


# Получить инфо о пользователе
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        return exact_user
    else:
        return 'В базе нет этого пользователя'


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Проверка данных через phone_number
def check_user_phone_number_db(phone_number):
    db = next(get_db())

    checker = db.query(User).filter(phone_number=phone_number).first()

    if checker:
        return checker
    else:
        return 'В базе нет такого номера телефона'


def edit_user_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'email':
            exact_user.email = new_info
        elif edit_info == 'country':
            exact_user.country = new_info

        db.commit()

        return f'Данные пользователя {user_id} были успешно изменены!'
    else:
        return 'В базе нет такого пользователя((('


def delete_user_db(user_id):
    db = next(get_db())

    user_to_delete = db.query(User).filter(user_id=user_id).first()

    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return 'Юзер успешно удалён'

from database import get_db
from database.models import UserCard
from datetime import datetime


# Добавление карты
def add_new_card_db(card_id, user_id, card_name, card_number, balance, exp_date):
    db = next(get_db())

    new_card = UserCard(card_id=card_id, user_id=user_id, card_name=card_name,
                        card_number=card_number, balance=balance, exp_date=exp_date)
    db.add(new_card)
    db.commit()
    return True


# Вывести все карты определённого пользователя
def get_exact_user_all_card_db(user_id):
    db = next(get_db())

    if user_id:
        exact_user_cards = db.query(UserCard).filter_by(user_id=user_id).all()
        return [i for i in exact_user_cards]


# Вывести определённую карту определённого пользователя
def get_exact_user_exact_card_db(user_id, card_id):
    db = next(get_db())

    if user_id:
        exact_user_exact_card = db.query(UserCard).filter_by(card_id=card_id).first()
        return exact_user_exact_card


# Проверка карты на наличие в бд
def check_card_in_db(card_id):
    db = next(get_db())

    check_card = db.query(UserCard).filter_by(card_id=card_id).first()
    if check_card:
        return check_card
    else:
        return 'В базе нет такой карты'


# Удаление карты
def card_to_delete_db(card_id):
    db = next(get_db())

    card_to_delete = db.query(UserCard).filter_by(card_id=card_id).first()
    db.delete(card_to_delete)
    db.commit()
    return 'Карта успешно удалена'


# Изменение информации на карте
def edit_info_on_card_db(card_id, edit_info, new_info):
    db = next(get_db())

    exact_card = db.query(card_id).filter_by(card_id=card_id).first()

    if exact_card:
        if edit_info == 'card_name':
            edit_info.card_name = new_info
        elif edit_info == 'card_number':
            edit_info.card_number = new_info
        elif edit_info == 'balance':
            edit_info.balance = new_info
        elif edit_info == 'exp_date':
            edit_info.exp_date = new_info

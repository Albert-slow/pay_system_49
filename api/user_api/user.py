from fastapi import APIRouter
from database.userservice import registration_user_db, get_exact_user_db, get_all_users_db,\
    edit_user_db, check_user_phone_number_db, delete_user_db
import re
from pydantic import BaseModel

user_router = APIRouter(prefix='/api/user', tags=['Работа с пользователями'])


class UserRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    country: str


@user_router.post('/register')
async def register_new_user(data: UserRegistrationValidator):
    new_user_data = data.model_dump()

    regex = re.match(r'^(\+998|998)\d{9}$', new_user_data.phone_number)

    if regex:
        return True
    else:
        return False

from sqlalchemy import Column, String, Integer, Boolean, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


class UserCard(Base):
    __tablename__ = "cards"
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    card_name = Column(String, nullable=False)
    card_number = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False, default=0)
    exp_date = Column(Integer, nullable=False)

    user_fk = relationship(User, lazy="subquery")


class Transfer(Base):
    __tablename__ = "transfers"
    trasfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey("cards.card_id"))
    card_to_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)

    status = Column(Boolean, default=True)

    trasaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, lazy="subquery")

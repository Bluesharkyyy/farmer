from sqlalchemy import func
from sqlalchemy.orm import aliased
from telebot import types
from models import User
from database import create_session


class GameService:

    def __init__(self):
        self.session = create_session()

    def get_user(self, tg_user: types.User) -> User | None:
        user = self.session.query(User).filter(User.telegram_id == tg_user.id).first()
        return user

    def get_friends_list(self, tg_user: types.User) -> list[User]:
        users = self.session.query(User).filter(User.inviter_id == tg_user.id).all()
        return users

    def check_user_or_register(self, tg_user: types.User) -> bool:
        user = self.get_user(tg_user)
        if not user:
            new_user = User(telegram_name=tg_user.username, telegram_id=tg_user.id)
            self.session.add(new_user)
            self.session.commit()
            return True
        return False
    
    def upgrade_level(self, tg_user: types.User) -> bool:
        user = self.get_user(tg_user)

        if user.balance < user.level ** 2:
            return False
        
        user.balance -= user.level ** 2
        user.level += 1
        self.session.commit()
        return True

    def give_startpack(self, tg_user: types.User, invite_code: int) -> str | None:
        user = self.get_user(tg_user)

        if user.id == tg_user.id:
            return "Вы не можете указать свой код."
        
        inviter = self.session.query(User).filter(User.inviter_id == invite_code).first()
        if not inviter:
            return "Указанный код не найден"

        if user.inviter.id:
            return "Вы уже получили стартовый набор"
        
        user.balance += 500
        user.inviter_id = invite_code
        self.session.commit()
        return None

    @staticmethod
    def update_coins():
        session = create_session()

        print("Обновление коинов....")

        Players = aliased(User)

        session.query(User).update({
            User.balance: User.balance + User.level + session.query(
                func.coalesce(func.sum(Players.level), 0) / 4
            ).filter(Players.inviter_id == User.telegram_id).scalar_subquery()
        })
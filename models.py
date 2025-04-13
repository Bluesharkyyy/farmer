from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_name = Column(String)
    telegram_id = Column(Integer, unique=True)
    level = Column(Integer, default=1) 
    balance = Column(Float, default=0)
    inviter_id = Column(Integer, ForeignKey("user.id"), nullable=True)


from sqlalchemy import Column, ForeignKey, Integer, String, Text, BigInteger
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    avatar = Column(String)
    email = Column(String)
    age = Column(Integer)
    city = Column(String)
    school = Column(String)
    clas = Column(String)

    first = Column(String)
    second = Column(String)

    user_id = Column(String, primary_key=True, unique=True, index=True)

    messages = relationship("Message", back_populates="user")


class Message(Base):
    __tablename__ = "messages"

    message_id_for_db = Column(Integer, primary_key=True, index=True)

    text = Column(Text, index=True)
    time = Column(BigInteger, index=True)

    message_id = Column(String, unique=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"))

    user = relationship("User", back_populates="messages")


class Chat(Base):
    __tablename__ = "chats"

    chat_id = Column(String, primary_key=True, unique=True, index=True)
    user_id_1 = Column(String, ForeignKey("users.user_id"))
    user_id_2 = Column(String, ForeignKey("users.user_id"))

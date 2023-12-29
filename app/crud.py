from sqlalchemy.orm import Session
from app import models, schemas

################################################################################
# User crud


def create_user(db: Session, user: schemas.UserCreate, user_id: str):
    db_user = models.User(
        avatar=user.avatar,
        email=user.email,
        age=user.age,
        city=user.city,
        school=user.school,
        clas=user.clas,
        user_id=user_id,
        first=user.first,
        second=user.second
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_user_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


################################################################################
# Message crud


def create_user_message(
    db: Session, message: schemas.MessageCreate, user_id: str, message_id: str
):
    db_message = models.Message(
        **message.dict(), user_id=user_id, message_id=message_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()


################################################################################
# Chat crud
def create_chat(
    db: Session, chat: schemas.ChatCreate, chat_id: str, user_id_1: str, user_id_2: str
):
    db_chat = models.Chat(chat_id=chat_id, user_id_1=user_id_1, user_id_2=user_id_2)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def get_chat_by_chat_id(db: Session, chat_id: str):
    return db.query(models.Chat).filter(models.Chat.chat_id == chat_id).first()


def get_chats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chat).offset(skip).limit(limit).all()


################################################################################
#Respomse user

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
import json

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


################################################################################
# User methods


@app.post("/users/{user_id}", response_model=schemas.User)
def create_user(user_id: str, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_user_id(db, user_id=user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user, user_id=user_id)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


################################################################################
# Message methods


@app.post("/users/{user_id}/{message_id}/messages/", response_model=schemas.Message)
def create_message_for_user(
    user_id: str,
    message_id: str,
    message: schemas.MessageCreate,
    db: Session = Depends(get_db),
):
    return crud.create_user_message(
        db=db, message=message, user_id=user_id, message_id=message_id
    )


@app.get("/messages/", response_model=list[schemas.Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages


################################################################################
# Chat methods


@app.post("/chats/{chat_id}/", response_model=schemas.Chat)
def create_chat(
    chat_id: str,
    user_id_1: str,
    user_id_2: str,
    chat: schemas.ChatCreate,
    db: Session = Depends(get_db),
):
    db_chat = crud.get_chat_by_chat_id(db, chat_id=chat_id)
    if db_chat:
        raise HTTPException(status_code=400, detail="Chat already created")
    return crud.create_chat(
        db=db, chat=chat, chat_id=chat_id, user_id_1=user_id_1, user_id_2=user_id_2
    )


@app.get("/chats/", response_model=list[schemas.Chat])
def read_chats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chats = crud.get_chats(db, skip=skip, limit=limit)
    return chats


################################################################################
# Response

class ProfileInfo:
    def __init__(self, user_id, firstname, secondname, school, city, age, clas, avatar):
        self.user_id = user_id
        self.firstname = firstname
        self.secondname = secondname
        self.school = school
        self.city = city
        self.age = age
        self.clas = clas
        self.avatar = avatar


def get_profile(user_id: int, user: schemas.User):
    profile_info = ProfileInfo(
        user_id=user_id,
        firstname=user.firstname,
        secondname=user.secondname,
        school=user.school,
        city=user.city,
        age=user.age,
        clas=user.clas,
        avatar=user.avatar,
    )

    response_data = {
        "user_id": profile_info.user_id,
        "firstname": profile_info.firstname,
        "secondname": profile_info.secondname,
        "school": profile_info.school,
        "city": profile_info.city,
        "age": profile_info.age,
        "class": profile_info.clas,
        "avatar": profile_info.avatar,
    }
    return json.dumps(response_data)


@app.get("/user/{user_id}/")
def read_users(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    return ProfileInfo(user)


################################################################################

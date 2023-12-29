from pydantic import BaseModel

################################################################################
# Message schema


class MessageBase(BaseModel):
    text: str
    time: int


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    message_id: str
    user_id: str

    class Config:
        from_attributes = True


################################################################################
# User schema


class UserBase(BaseModel):
    avatar: str
    email: str
    age: int
    city: str
    school: str
    clas: str
    first: str
    second: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: str
    messages: list[Message] = []

    class Config:
        from_attributes = True


################################################################################
# Chat schema


class ChatBase(BaseModel):
    pass


class ChatCreate(ChatBase):
    pass


class Chat(ChatBase):
    chat_id: str
    user_id_1: str
    user_id_2: str

    class Config:
        from_attributes = True


################################################################################

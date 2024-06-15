from sqlmodel import SQLModel,Field
from typing import Optional

class User(SQLModel, table=True):
    User_id: Optional[int] = Field(None, primary_key=True)
    User_name: str
    user_email: str
    # optional todo
    # phone_number:int
    user_password: str
    



class Token(SQLModel, table=True):
    token_id: Optional[int] = Field(None, primary_key=True)
    refresh_token: str
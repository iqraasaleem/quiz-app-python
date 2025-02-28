from sqlmodel import SQLModel,Field
from typing import Optional


class Admin(SQLModel, table=True):
    admin_id: Optional[int] = Field(None, primary_key=True)
    admin_email: str
    admin_name: str
    admin_password: str


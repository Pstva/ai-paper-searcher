import datetime
from enum import Enum

from sqlmodel import SQLModel


class UserType(str, Enum):
    user = "user"
    admin = "admin"


class UserCreate(SQLModel):
    email: str
    name: str
    password: str
    balance: int | None = None


class UserRead(SQLModel):
    id: int
    email: str
    name: str
    created_at: datetime.datetime
    balance: int


class UserUpdate(SQLModel):
    name: str | None = None
    password: str | None = None
    user_type: str | None = None
    balance: int | None = None


class UserDelete(SQLModel):
    email: str | None = None
    id: int | None = None

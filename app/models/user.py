import datetime
from typing import TYPE_CHECKING

from schemas.user import UserType
from sqlmodel import Field, Relationship, SQLModel
from utils.utils import get_current_datetime

if TYPE_CHECKING:
    from models.chat_request import ChatCompletionRequest
    from models.transaction import Transaction


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(description="User name")
    email: str = Field(
        unique=True,
        index=True,
        description="User email",
    )
    user_type: UserType = Field(default=UserType.user)
    created_at: datetime.datetime = Field(default_factory=get_current_datetime)
    balance: int = Field(default=0, ge=0)

    # relationships
    transactions: list["Transaction"] = Relationship(
        back_populates="creator",
        sa_relationship_kwargs={"cascade": "all, delete-orphan", "lazy": "selectin"},
    )
    password_hash: str

    chat_requests: list["ChatCompletionRequest"] = Relationship(
        back_populates="creator",
        sa_relationship_kwargs={"cascade": "all, delete-orphan", "lazy": "selectin"},
    )

    class Config:
        """Model configuration"""

        validate_assignment = True

import datetime
from typing import TYPE_CHECKING, Optional

from schemas.transaction import TransactionStatus, TransactionType
from sqlmodel import Field, Relationship, SQLModel
from utils.utils import get_current_datetime

if TYPE_CHECKING:
    from models.chat_request import ChatCompletionRequest
    from models.user import User


class Transaction(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    transaction_type: TransactionType
    transaction_status: TransactionStatus = Field(default=TransactionStatus.pending)
    created_at: datetime.datetime = Field(default_factory=get_current_datetime)
    processed_at: Optional[datetime.datetime] = Field(default=None)

    # relationships
    creator: Optional["User"] = Relationship(
        back_populates="transactions",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    creator_id: Optional["int"] = Field(default=None, foreign_key="user.id", index=True)
    chat_request: Optional["ChatCompletionRequest"] = Relationship(
        back_populates="assigned_transaction",
        sa_relationship_kwargs={"cascade": "all, delete-orphan", "lazy": "selectin"},
    )

    class Config:
        """Model configuration"""

        validate_assignment = True

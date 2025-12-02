import datetime
from typing import TYPE_CHECKING, Optional

from schemas.chat_request import RequestStatus
from sqlmodel import JSON, Column, Field, Relationship, SQLModel
from utils.utils import get_current_datetime

if TYPE_CHECKING:
    from models.chat_response import ChatResponse
    from models.transaction import Transaction
    from models.user import User


class ChatCompletionRequest(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    model: str
    messages: list[dict, str] = Field(sa_column=Column(JSON), default_factory=list)
    max_tokens: int = Field(default=512, ge=0)
    temperature: float = Field(default=0.0, ge=0, le=1)
    top_p: float = Field(default=1, ge=0, le=1)
    frequency_penalty: float = Field(default=1, ge=-2, le=2)
    cost: int
    created_at: datetime.datetime = Field(default_factory=get_current_datetime)
    status: RequestStatus = Field(default=RequestStatus.created)
    updated_at: datetime.datetime | None = Field(default=None)
    finished_at: datetime.datetime | None = Field(default=None)
    # relationships
    creator: Optional["User"] = Relationship(
        back_populates="chat_requests",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    creator_id: Optional["int"] = Field(default=None, foreign_key="user.id", index=True)
    assigned_transaction: Optional["Transaction"] = Relationship(
        back_populates="chat_request",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    assigned_transaction_id: int | None = Field(
        default=None, foreign_key="transaction.id"
    )
    response: Optional["ChatResponse"] = Relationship(
        back_populates="request",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    class Config:
        """Model configuration"""

        validate_assignment = True

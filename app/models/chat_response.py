import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from utils.utils import get_current_datetime

if TYPE_CHECKING:
    from models.chat_request import ChatCompletionRequest


class ChatResponse(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    output: str | None = Field(default=None)
    error: str | None = Field(default=None)
    created_at: datetime.datetime = Field(default_factory=get_current_datetime)
    updated_at: datetime.datetime | None = Field(default=None)
    finished_at: datetime.datetime | None = Field(default=None)

    # relationships
    request: Optional["ChatCompletionRequest"] = Relationship(
        back_populates="response",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    request_id: int | None = Field(default=None, foreign_key="chatcompletionrequest.id")

    class Config:
        """Model configuration"""

        validate_assignment = True

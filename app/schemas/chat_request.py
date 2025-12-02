import datetime
from enum import Enum

from sqlmodel import SQLModel


class MessageType(str, Enum):
    user = "user"
    system = "system"
    assistant = "assistant"


class RequestStatus(str, Enum):
    created = "created"
    pending = "pending"
    succeeded = "succeeded"
    failed = "failed"
    cancelled = "cancelled"


class Message(SQLModel):
    role: MessageType
    content: str


class ChatCompletionRequestCreate(SQLModel):
    model: str
    messages: list[Message]
    cost: int
    max_tokens: int | None = None
    temperature: float | None = None
    top_p: float | None = None
    frequency_penalty: float | None = None


class ChatCompletionRequestUpdate(SQLModel):
    status: RequestStatus | None = None
    updated_at: datetime.datetime | None = None
    finished_at: datetime.datetime | None = None

from sqlmodel import SQLModel


class ChatResponseCreate(SQLModel):
    output: str | None = None
    error: str | None = None
    metadata: dict | None = None

import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Message:
    def __init__(
        self, role: str, content: any, created_at: datetime.datetime | None = None
    ) -> None:
        self.role = role
        self.content = content
        if self.created_at is None:
            self.created_at = created_at
        self.created_at = datetime.datetime.now()

    def to_message_format(self) -> list[dict[str, str]]:
        return {"role": self.role, "content": self.content}


class ChatHistory:
    def __init__(
        self,
        messages: list[Message],
    ) -> None:
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.messages = messages
        self.formatted_messages = self.__to_messages_format(messages=self.messages)

    def add_message_to_chat(self, message: Message):
        self.updated_at = datetime.datetime.now()
        self.messages.append(message)
        self.__add_new_message_formatted(message)

    def __to_messages_format(
        self, messages: list[Message]
    ) -> list[list[dict[str, str]]]:
        all_messages = []
        for message in messages:
            all_messages.append(message.to_message_format())
        return all_messages

    def __add_new_message_formatted(self, message: Message):
        self.formatted_messages = self.formatted_messages.append()

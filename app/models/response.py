import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chat import ChatHistory


class Response:
    pass


class TextResponse:
    def __init__(self, response: str, chat_history: ChatHistory):
        self.response = response
        self.chat_history = chat_history
        self.created_at = datetime.datetime.now()

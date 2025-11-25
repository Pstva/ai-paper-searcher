from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chat import ChatHistory, Message
    from .user import User


class UserRequest:
    def __init__(self, user: User, chat_history: ChatHistory) -> None:
        self.user = user
        self.chat_history = chat_history


class TextRequest(UserRequest):
    def __init__(self, user: User, chat_history: ChatHistory, text: str) -> None:
        super.__init__(self, user=user, chat_history=chat_history)
        self.message = Message(role="user", content=text)


class AudioRequest(UserRequest):
    def __init__(self, user: User, chat_history: ChatHistory, audio_path: str) -> None:
        super.__init__(self, user=user, chat_history=chat_history)
        self.message = Message(
            role="user",
            content=[
                {
                    "type": "audio_url",
                    "audio_url": {"url": audio_path},
                }
            ],
        )

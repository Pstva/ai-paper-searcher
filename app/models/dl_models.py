from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Model(ABC):
    def __init__(self, model_url: str, model: str) -> None:
        self.model_url = model_url
        self.model = model


class STTModel(Model):
    """Speech-to-text neural model."""

    def __init__(self, model_url: str, model: str) -> None:
        super().__init__(model_url=model_url, model=model)
        pass

    def transcribe_audio_to_text(self, *args) -> str:
        raise NotImplementedError


class WhisperSTTModel(STTModel):
    def __init__(self, model_url: str, model: str) -> None:
        super().__init__(model_url=model_url, model=model)

    def transcribe_audio_to_text(
        self, audio_path: str | None = None, **generation_kwargs
    ) -> str:
        # здесь будет запрос к модели, поднятой на vllm|sglang или еще как-то,
        # пока просто схематично напишу
        # output_text = asr(audio_path, **generation_kwargs)
        # return output_text
        raise NotImplementedError


class LLMModel(Model):
    def __init__(self, model_url: str, model: str) -> None:
        super().__init__(model_url=model_url, model=model)

    def make_request(self, messages: list[dict[str, str]], **generation_kwargs) -> str:
        # здесь будет запрос к модели, которая в свою очередь вызывает mcp tool для поиска статей
        # поднятой на sglang, пока просто примерно схематично напишу
        # response = asr(audio_path, **generation_kwargs)
        # return response
        raise NotImplementedError

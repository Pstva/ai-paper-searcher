from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dl_models import LLMModel, WhisperSTTModel
    from .request import AudioRequest, TextRequest
    from .response import TextResponse

REQUEST_COST = 1


class RequestHandler:
    """Class for handling a request from users."""

    def __init__(
        self,
        llm_model: LLMModel,
        stt_model: WhisperSTTModel,
    ):
        self.llm_model = llm_model
        self.stt_model = stt_model

    def process_request(self, request: TextRequest | AudioRequest, **generation_kwargs):

        if request.user.balance.balance <= 0:
            raise ValueError("Your balance is 0. Please, top up it first.")

        if isinstance(request, AudioRequest):
            transcribed_text = self.stt_model.transcribe_audio_to_text(
                AudioRequest.message.content[0]["audio_url"]
            )
            text_request = TextRequest(
                user=request.user,
                chat_history=request.chat_history,
                text=transcribed_text,
            )
        else:
            text_request = request

        messages = text_request.chat_history.add_message_to_chat(
            message=text_request.message
        )
        response = self.llm_model.make_request(messages=messages, **generation_kwargs)

        # пока так, позже обдумаю схему пополнения и снятия с баланса
        text_request.user -= REQUEST_COST

        return TextResponse(response=response, chat_history=text_request.chat_history)

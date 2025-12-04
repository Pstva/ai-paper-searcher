from enum import Enum

from pydantic import AnyHttpUrl, BaseModel

# TODO: прописать нормально, когда до конца разберусь, как будет происходить взаимодействие с моделями


class ModelType(str, Enum):
    stt = "stt"
    llm = "llm"


class Model(BaseModel):
    model_url: AnyHttpUrl
    model_name: str
    type: ModelType

from pydantic import BaseModel, TypeAdapter, Field
from typing import Optional, Literal, Union

# SenseData
###########


class Message(BaseModel):
    username: str
    message: str


class Entity(BaseModel):
    entityID: str
    type: str


class SenseData(BaseModel):

    last_message: Optional[Message]
    is_raining: bool
    is_day: bool
    entities: list[Entity]


# Actions
#########


class ChatAction(BaseModel):
    action: Literal["chat"] = Field(..., description="Announce a message to the world.")
    message: str


class MoveAction(BaseModel):
    action: Literal["move"] = Field(..., description="Move towards an entity.")
    entityID: str


Action = Union[ChatAction, MoveAction]
ActionType = TypeAdapter(Action)

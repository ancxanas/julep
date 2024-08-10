# generated by datamodel-codegen:
#   filename:  openapi-0.4.0.yaml

from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel

from .Tools import ChosenToolCall, Tool, ToolResponse


class BaseEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    role: Literal[
        "user",
        "agent",
        "system",
        "function",
        "function_response",
        "function_call",
        "auto",
    ]
    """
    ChatML role (system|assistant|user|function_call|function|function_response|auto)
    """
    name: str | None = None
    content: (
        list[ChatMLTextContentPart | ChatMLImageContentPart]
        | Tool
        | ChosenToolCall
        | str
        | ToolResponse
        | list[
            list[ChatMLTextContentPart | ChatMLImageContentPart]
            | Tool
            | ChosenToolCall
            | str
            | ToolResponse
        ]
    )
    source: Literal[
        "api_request", "api_response", "tool_response", "internal", "summarizer", "meta"
    ]
    tokenizer: str | None = None
    token_count: int | None = None
    timestamp: Annotated[float, Field(ge=0.0)]
    """
    This is the time that this event refers to.
    """


class ChatMLImageContentPart(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    image_url: ImageURL
    """
    The image URL
    """
    type: Literal["image_url"] = "image_url"
    """
    The type (fixed to 'image_url')
    """


class ChatMLMessage(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    role: Literal[
        "user",
        "agent",
        "system",
        "function",
        "function_response",
        "function_call",
        "auto",
    ]
    """
    The role of the message
    """
    content: str | list[str] | list[ChatMLTextContentPart | ChatMLImageContentPart]
    """
    The content parts of the message
    """
    name: str | None = None
    """
    Name
    """
    tool_calls: Annotated[
        list[ChosenToolCall], Field([], json_schema_extra={"readOnly": True})
    ]
    """
    Tool calls generated by the model.
    """
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]


class ChatMLTextContentPart(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    text: str
    type: Literal["text"] = "text"
    """
    The type (fixed to 'text')
    """


class Entry(BaseEntry):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]


class History(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    entries: list[BaseEntry]
    relations: list[Relation]
    session_id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """


class ImageURL(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: AnyUrl
    """
    Image URL or base64 data url (e.g. `data:image/jpeg;base64,<the base64 encoded image>`)
    """
    detail: Literal["low", "high", "auto"] = "auto"
    """
    The detail level of the image
    """


class InputChatMLMessage(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    role: Literal[
        "user",
        "agent",
        "system",
        "function",
        "function_response",
        "function_call",
        "auto",
    ]
    """
    The role of the message
    """
    content: str | list[str] | list[ChatMLTextContentPart | ChatMLImageContentPart]
    """
    The content parts of the message
    """
    name: str | None = None
    """
    Name
    """
    continue_: Annotated[bool | None, Field(None, alias="continue")]
    """
    Whether to continue this message or return a new one
    """


class Relation(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    head: UUID
    relation: str
    tail: UUID

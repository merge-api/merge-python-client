# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_schema import ItemSchema
from .remote_field_class_field_choices_item import RemoteFieldClassFieldChoicesItem
from .remote_field_class_field_format import RemoteFieldClassFieldFormat
from .remote_field_class_field_type import RemoteFieldClassFieldType


class RemoteFieldClass(UniversalBaseModel):
    id: typing.Optional[str]
    display_name: typing.Optional[str]
    remote_key_name: typing.Optional[str]
    description: typing.Optional[str]
    is_custom: typing.Optional[bool]
    is_required: typing.Optional[bool]
    field_type: typing.Optional[RemoteFieldClassFieldType]
    field_format: typing.Optional[RemoteFieldClassFieldFormat]
    field_choices: typing.Optional[typing.List[RemoteFieldClassFieldChoicesItem]]
    item_schema: typing.Optional[ItemSchema]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

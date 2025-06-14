# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .field_format_enum import FieldFormatEnum
from .field_type_enum import FieldTypeEnum
from .item_schema import ItemSchema


class RemoteFieldClass(UncheckedBaseModel):
    id: typing.Optional[str] = None
    display_name: typing.Optional[str] = None
    remote_key_name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    is_custom: typing.Optional[bool] = None
    is_required: typing.Optional[bool] = None
    field_type: typing.Optional[FieldTypeEnum] = None
    field_format: typing.Optional[FieldFormatEnum] = None
    field_choices: typing.Optional[typing.List[str]] = None
    item_schema: typing.Optional[ItemSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

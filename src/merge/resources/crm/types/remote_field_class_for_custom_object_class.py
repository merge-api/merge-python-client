# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
import pydantic
from .remote_field_class_for_custom_object_class_field_type import RemoteFieldClassForCustomObjectClassFieldType
from .remote_field_class_for_custom_object_class_field_format import RemoteFieldClassForCustomObjectClassFieldFormat
from .remote_field_class_for_custom_object_class_field_choices_item import (
    RemoteFieldClassForCustomObjectClassFieldChoicesItem,
)
from .remote_field_class_for_custom_object_class_item_schema import RemoteFieldClassForCustomObjectClassItemSchema
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RemoteFieldClassForCustomObjectClass(UniversalBaseModel):
    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    display_name: typing.Optional[str]
    remote_key_name: typing.Optional[str]
    description: typing.Optional[str]
    is_required: typing.Optional[bool]
    field_type: typing.Optional[RemoteFieldClassForCustomObjectClassFieldType]
    field_format: typing.Optional[RemoteFieldClassForCustomObjectClassFieldFormat]
    field_choices: typing.Optional[typing.List[RemoteFieldClassForCustomObjectClassFieldChoicesItem]]
    item_schema: typing.Optional[RemoteFieldClassForCustomObjectClassItemSchema]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

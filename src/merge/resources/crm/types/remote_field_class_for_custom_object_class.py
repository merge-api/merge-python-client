# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_field_class_for_custom_object_class_field_choices_item import (
    RemoteFieldClassForCustomObjectClassFieldChoicesItem,
)
from .remote_field_class_for_custom_object_class_field_format import RemoteFieldClassForCustomObjectClassFieldFormat
from .remote_field_class_for_custom_object_class_field_type import RemoteFieldClassForCustomObjectClassFieldType
from .remote_field_class_for_custom_object_class_item_schema import RemoteFieldClassForCustomObjectClassItemSchema


class RemoteFieldClassForCustomObjectClass(pydantic.BaseModel):
    display_name: typing.Optional[str]
    remote_key_name: typing.Optional[str]
    description: typing.Optional[str]
    is_required: typing.Optional[bool]
    field_type: typing.Optional[RemoteFieldClassForCustomObjectClassFieldType]
    field_format: typing.Optional[RemoteFieldClassForCustomObjectClassFieldFormat]
    field_choices: typing.Optional[typing.List[RemoteFieldClassForCustomObjectClassFieldChoicesItem]]
    item_schema: typing.Optional[RemoteFieldClassForCustomObjectClassItemSchema]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

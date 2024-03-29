# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .cardinality_enum import CardinalityEnum
from .object_class_description_request import ObjectClassDescriptionRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AssociationTypeRequestRequest(pydantic.BaseModel):
    source_object_class: ObjectClassDescriptionRequest
    target_object_classes: typing.List[ObjectClassDescriptionRequest]
    remote_key_name: str
    display_name: typing.Optional[str]
    cardinality: typing.Optional[CardinalityEnum]
    is_required: typing.Optional[bool]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}

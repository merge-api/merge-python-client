# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .field_mapping_api_instance import FieldMappingApiInstance

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FieldMappingApiInstanceResponse(pydantic.BaseModel):
    file: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="File")
    folder: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Folder")
    drive: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Drive")
    group: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Group")
    user: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="User")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}

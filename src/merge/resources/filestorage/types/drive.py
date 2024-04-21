# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Drive(pydantic.BaseModel):
    """
    # The Drive Object

    ### Description

    The `Drive` object is used to represent a drive that contains the folders and files in the user's workspace.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/drives` endpoint and view their drives.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    name: typing.Optional[str] = pydantic.Field(description="The drive's name.")
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's drive was created."
    )
    drive_url: typing.Optional[str] = pydantic.Field(description="The drive's url.")
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Any]]]]

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

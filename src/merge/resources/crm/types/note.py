# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .note_account import NoteAccount
from .note_contact import NoteContact
from .note_opportunity import NoteOpportunity
from .note_owner import NoteOwner
from .remote_data import RemoteData
from .remote_field import RemoteField


class Note(pydantic.BaseModel):
    """
    # The Note Object
    ### Description
    The `Note` object is used to represent a note on another object.
    ### Usage Example
    TODO
    """

    owner: typing.Optional[NoteOwner] = pydantic.Field(description="The note's owner.")
    content: typing.Optional[str] = pydantic.Field(description="The note's content.")
    contact: typing.Optional[NoteContact] = pydantic.Field(description="The note's contact.")
    account: typing.Optional[NoteAccount] = pydantic.Field(description="The note's account.")
    opportunity: typing.Optional[NoteOpportunity] = pydantic.Field(description="The note's opportunity.")
    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's lead was updated."
    )
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's lead was created."
    )
    remote_was_deleted: typing.Optional[bool]
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

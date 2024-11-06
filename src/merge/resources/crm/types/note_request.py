# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .note_request_owner import NoteRequestOwner
import pydantic
from .note_request_contact import NoteRequestContact
from .note_request_account import NoteRequestAccount
from .note_request_opportunity import NoteRequestOpportunity
from .remote_field_request import RemoteFieldRequest
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class NoteRequest(UniversalBaseModel):
    """
    # The Note Object

    ### Description

    The `Note` object is used to represent a note on another object.

    ### Usage Example

    TODO
    """

    owner: typing.Optional[NoteRequestOwner] = pydantic.Field(default=None)
    """
    The note's owner.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The note's content.
    """

    contact: typing.Optional[NoteRequestContact] = pydantic.Field(default=None)
    """
    The note's contact.
    """

    account: typing.Optional[NoteRequestAccount] = pydantic.Field(default=None)
    """
    The note's account.
    """

    opportunity: typing.Optional[NoteRequestOpportunity] = pydantic.Field(default=None)
    """
    The note's opportunity.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

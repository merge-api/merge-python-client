# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .note_request_account import NoteRequestAccount
from .note_request_contact import NoteRequestContact
from .note_request_opportunity import NoteRequestOpportunity
from .note_request_owner import NoteRequestOwner
from .remote_field_request import RemoteFieldRequest


class NoteRequest(UniversalBaseModel):
    """
    # The Note Object

    ### Description

    The `Note` object is used to represent a note on another object.

    ### Usage Example

    TODO
    """

    owner: typing.Optional[NoteRequestOwner] = pydantic.Field()
    """
    The note's owner.
    """

    content: typing.Optional[str] = pydantic.Field()
    """
    The note's content.
    """

    contact: typing.Optional[NoteRequestContact] = pydantic.Field()
    """
    The note's contact.
    """

    account: typing.Optional[NoteRequestAccount] = pydantic.Field()
    """
    The note's account.
    """

    opportunity: typing.Optional[NoteRequestOpportunity] = pydantic.Field()
    """
    The note's opportunity.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

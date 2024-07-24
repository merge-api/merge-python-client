# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact_request_account import ContactRequestAccount


class ContactRequest(UniversalBaseModel):
    """
    # The Contact Object

    ### Description

    The `Contact` object is used to represent the customer, lead, or external user that a ticket is associated with.

    ### Usage Example

    TODO
    """

    name: typing.Optional[str] = pydantic.Field()
    """
    The contact's name.
    """

    email_address: typing.Optional[str] = pydantic.Field()
    """
    The contact's email address.
    """

    phone_number: typing.Optional[str] = pydantic.Field()
    """
    The contact's phone number.
    """

    details: typing.Optional[str] = pydantic.Field()
    """
    The contact's details.
    """

    account: typing.Optional[ContactRequestAccount] = pydantic.Field()
    """
    The contact's account.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

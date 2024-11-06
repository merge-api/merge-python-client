# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class AccountingPhoneNumberRequest(UniversalBaseModel):
    """
    # The AccountingPhoneNumber Object

    ### Description

    The `AccountingPhoneNumber` object is used to represent a contact's or company's phone number.

    ### Usage Example

    Fetch from the `GET CompanyInfo` endpoint and view the company's phone numbers.
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number's type.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .phone_number_request_phone_number_type import PhoneNumberRequestPhoneNumberType
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class PhoneNumberRequest(UniversalBaseModel):
    """
    # The PhoneNumber Object

    ### Description

    The `PhoneNumber` object is used to represent a candidate's phone number.

    ### Usage Example

    Fetch from the `GET Candidate` endpoint and view their phone numbers.
    """

    value: typing.Optional[str] = pydantic.Field()
    """
    The phone number.
    """

    phone_number_type: typing.Optional[PhoneNumberRequestPhoneNumberType] = pydantic.Field()
    """
    The type of phone number.
    
    - `HOME` - HOME
    - `WORK` - WORK
    - `MOBILE` - MOBILE
    - `SKYPE` - SKYPE
    - `OTHER` - OTHER
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

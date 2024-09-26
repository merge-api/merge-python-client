# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .activity_request_user import ActivityRequestUser
import pydantic
from .activity_request_activity_type import ActivityRequestActivityType
from .activity_request_visibility import ActivityRequestVisibility
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class ActivityRequest(UniversalBaseModel):
    """
    # The Activity Object

    ### Description

    The `Activity` object is used to represent an activity for a candidate performed by a user.

    ### Usage Example

    Fetch from the `LIST Activities` endpoint and filter by `ID` to show all activities.
    """

    user: typing.Optional[ActivityRequestUser] = pydantic.Field()
    """
    The user that performed the action.
    """

    activity_type: typing.Optional[ActivityRequestActivityType] = pydantic.Field()
    """
    The activity's type.
    
    - `NOTE` - NOTE
    - `EMAIL` - EMAIL
    - `OTHER` - OTHER
    """

    subject: typing.Optional[str] = pydantic.Field()
    """
    The activity's subject.
    """

    body: typing.Optional[str] = pydantic.Field()
    """
    The activity's body.
    """

    visibility: typing.Optional[ActivityRequestVisibility] = pydantic.Field()
    """
    The activity's visibility.
    
    - `ADMIN_ONLY` - ADMIN_ONLY
    - `PUBLIC` - PUBLIC
    - `PRIVATE` - PRIVATE
    """

    candidate: typing.Optional[str]
    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .earning_type import EarningType
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Earning(UniversalBaseModel):
    """
    # The Earning Object

    ### Description

    The `Earning` object is used to represent an array of different compensations that an employee receives within specific wage categories.

    ### Usage Example

    Fetch from the `LIST Earnings` endpoint and filter by `ID` to show all earnings.
    """

    id: typing.Optional[str] = None
    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    employee_payroll_run: typing.Optional[str] = None
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount earned.
    """

    type: typing.Optional[EarningType] = pydantic.Field(default=None)
    """
    The type of earning.
    
    - `SALARY` - SALARY
    - `REIMBURSEMENT` - REIMBURSEMENT
    - `OVERTIME` - OVERTIME
    - `BONUS` - BONUS
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_data: typing.Optional[typing.List[RemoteData]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

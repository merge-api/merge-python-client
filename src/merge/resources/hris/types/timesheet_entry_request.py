# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class TimesheetEntryRequest(UniversalBaseModel):
    """
    # The Timesheet Entry Object

    ### Description

    The `Timesheet Entry` object is used to track coverage for hours worked by an 'Employee'.

    ### Usage Example

    GET and POST Timesheet Entries
    """

    employee: typing.Optional[str] = pydantic.Field()
    """
    The employee the timesheet entry is for.
    """

    hours_worked: typing.Optional[float] = pydantic.Field()
    """
    The number of hours logged by the employee.
    """

    start_time: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The time at which the employee started work.
    """

    end_time: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The time at which the employee ended work.
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

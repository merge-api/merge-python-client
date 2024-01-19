# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UnitsEnum(str, enum.Enum):
    """
    - `HOURS` - HOURS
    - `DAYS` - DAYS
    """

    HOURS = "HOURS"
    DAYS = "DAYS"

    def visit(self, hours: typing.Callable[[], T_Result], days: typing.Callable[[], T_Result]) -> T_Result:
        if self is UnitsEnum.HOURS:
            return hours()
        if self is UnitsEnum.DAYS:
            return days()

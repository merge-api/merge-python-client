# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskStatusEnum(str, enum.Enum):
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaskStatusEnum.OPEN:
            return open()
        if self is TaskStatusEnum.CLOSED:
            return closed()

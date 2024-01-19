# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobStatusEnum(str, enum.Enum):
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `DRAFT` - DRAFT
    - `ARCHIVED` - ARCHIVED
    - `PENDING` - PENDING
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    DRAFT = "DRAFT"
    ARCHIVED = "ARCHIVED"
    PENDING = "PENDING"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
        draft: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatusEnum.OPEN:
            return open()
        if self is JobStatusEnum.CLOSED:
            return closed()
        if self is JobStatusEnum.DRAFT:
            return draft()
        if self is JobStatusEnum.ARCHIVED:
            return archived()
        if self is JobStatusEnum.PENDING:
            return pending()

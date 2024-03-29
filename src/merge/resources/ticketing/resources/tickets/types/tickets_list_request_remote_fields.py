# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TicketsListRequestRemoteFields(str, enum.Enum):
    PRIORITY = "priority"
    PRIORITY_STATUS = "priority,status"
    PRIORITY_STATUS_TICKET_TYPE = "priority,status,ticket_type"
    PRIORITY_TICKET_TYPE = "priority,ticket_type"
    STATUS = "status"
    STATUS_TICKET_TYPE = "status,ticket_type"
    TICKET_TYPE = "ticket_type"

    def visit(
        self,
        priority: typing.Callable[[], T_Result],
        priority_status: typing.Callable[[], T_Result],
        priority_status_ticket_type: typing.Callable[[], T_Result],
        priority_ticket_type: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        status_ticket_type: typing.Callable[[], T_Result],
        ticket_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TicketsListRequestRemoteFields.PRIORITY:
            return priority()
        if self is TicketsListRequestRemoteFields.PRIORITY_STATUS:
            return priority_status()
        if self is TicketsListRequestRemoteFields.PRIORITY_STATUS_TICKET_TYPE:
            return priority_status_ticket_type()
        if self is TicketsListRequestRemoteFields.PRIORITY_TICKET_TYPE:
            return priority_ticket_type()
        if self is TicketsListRequestRemoteFields.STATUS:
            return status()
        if self is TicketsListRequestRemoteFields.STATUS_TICKET_TYPE:
            return status_ticket_type()
        if self is TicketsListRequestRemoteFields.TICKET_TYPE:
            return ticket_type()

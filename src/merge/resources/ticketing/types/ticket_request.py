# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ....core.unchecked_base_model import UncheckedBaseModel
from .remote_field_request import RemoteFieldRequest
from .ticket_request_access_level import TicketRequestAccessLevel
from .ticket_request_account import TicketRequestAccount
from .ticket_request_assigned_teams_item import TicketRequestAssignedTeamsItem
from .ticket_request_assignees_item import TicketRequestAssigneesItem
from .ticket_request_attachments_item import TicketRequestAttachmentsItem
from .ticket_request_collections_item import TicketRequestCollectionsItem
from .ticket_request_contact import TicketRequestContact
from .ticket_request_creator import TicketRequestCreator
from .ticket_request_parent_ticket import TicketRequestParentTicket
from .ticket_request_priority import TicketRequestPriority
from .ticket_request_status import TicketRequestStatus


class TicketRequest(UncheckedBaseModel):
    """
    # The Ticket Object
    ### Description
    The `Ticket` object is used to represent a ticket, issue, task or case.
    ### Usage Example
    TODO
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's name.
    """

    assignees: typing.Optional[typing.List[typing.Optional[TicketRequestAssigneesItem]]] = pydantic.Field(default=None)
    """
    The individual `Users` who are assigned to this ticket. This does not include `Users` who just have view access to this ticket. To fetch all `Users` and `Teams` that can access the ticket, use the `GET /tickets/{ticket_id}/viewers` [endpoint](https://docs.merge.dev/ticketing/tickets/#tickets_viewers_list).
    """

    assigned_teams: typing.Optional[typing.List[typing.Optional[TicketRequestAssignedTeamsItem]]] = pydantic.Field(
        default=None
    )
    """
    The `Teams` that are assigned to this ticket. This does not include `Teams` who just have view access to this ticket. To fetch all `Users` and `Teams` that can access this ticket, use the `GET /tickets/{ticket_id}/viewers` [endpoint](https://docs.merge.dev/ticketing/tickets/#tickets_viewers_list).
    """

    creator: typing.Optional[TicketRequestCreator] = pydantic.Field(default=None)
    """
    The user who created this ticket.
    """

    due_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The ticket's due date.
    """

    status: typing.Optional[TicketRequestStatus] = pydantic.Field(default=None)
    """
    The current status of the ticket.
    
    * `OPEN` - OPEN
    * `CLOSED` - CLOSED
    * `IN_PROGRESS` - IN_PROGRESS
    * `ON_HOLD` - ON_HOLD
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket’s description. HTML version of description is mapped if supported by the third-party platform.
    """

    collections: typing.Optional[typing.List[typing.Optional[TicketRequestCollectionsItem]]] = pydantic.Field(
        default=None
    )
    """
    The `Collections` that this `Ticket` is included in.
    """

    ticket_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub category of the ticket within the 3rd party system. Examples include incident, task, subtask or to-do.
    """

    account: typing.Optional[TicketRequestAccount] = pydantic.Field(default=None)
    """
    The account associated with the ticket.
    """

    contact: typing.Optional[TicketRequestContact] = pydantic.Field(default=None)
    """
    The contact associated with the ticket.
    """

    parent_ticket: typing.Optional[TicketRequestParentTicket] = pydantic.Field(default=None)
    """
    The ticket's parent ticket.
    """

    attachments: typing.Optional[typing.List[typing.Optional[TicketRequestAttachmentsItem]]] = None
    access_level: typing.Optional[TicketRequestAccessLevel] = pydantic.Field(default=None)
    """
    The description of who is able to access a given ticket, or where access is inherited from.
    
    * `COMPANY` - COMPANY
    * `PUBLIC` - PUBLIC
    * `PRIVATE` - PRIVATE
    * `COLLECTION` - COLLECTION
    """

    tags: typing.Optional[typing.List[typing.Optional[str]]] = None
    roles: typing.Optional[typing.List[typing.Optional[str]]] = None
    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the ticket was completed.
    """

    ticket_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 3rd party url of the Ticket.
    """

    priority: typing.Optional[TicketRequestPriority] = pydantic.Field(default=None)
    """
    The priority or urgency of the Ticket.
    
    * `URGENT` - URGENT
    * `HIGH` - HIGH
    * `NORMAL` - NORMAL
    * `LOW` - LOW
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .collection import Collection  # noqa: E402, F401, I001
from .attachment import Attachment  # noqa: E402, F401, I001
from .ticket import Ticket  # noqa: E402, F401, I001

update_forward_refs(TicketRequest)

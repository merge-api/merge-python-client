# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .collection import Collection
import typing
import pydantic
import datetime as dt
from .ticket_assignees_item import TicketAssigneesItem
from .ticket_creator import TicketCreator
from .ticket_status import TicketStatus
from .ticket_collections_item import TicketCollectionsItem
from .ticket_account import TicketAccount
from .ticket_contact import TicketContact
from .ticket_priority import TicketPriority
from .remote_data import RemoteData
from .remote_field import RemoteField
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class Ticket(UniversalBaseModel):
    """
    # The Ticket Object

    ### Description

    The `Ticket` object is used to represent a ticket or a task within a system.

    ### Usage Example

    TODO
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

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's name.
    """

    assignees: typing.Optional[typing.List[typing.Optional[TicketAssigneesItem]]] = None
    creator: typing.Optional[TicketCreator] = pydantic.Field(default=None)
    """
    The user who created this ticket.
    """

    due_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The ticket's due date.
    """

    status: typing.Optional[TicketStatus] = pydantic.Field(default=None)
    """
    The current status of the ticket.
    
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `IN_PROGRESS` - IN_PROGRESS
    - `ON_HOLD` - ON_HOLD
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket’s description. HTML version of description is mapped if supported by the third-party platform.
    """

    collections: typing.Optional[typing.List[typing.Optional[TicketCollectionsItem]]] = None
    ticket_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub category of the ticket within the 3rd party system. Examples include incident, task, subtask or to-do.
    """

    account: typing.Optional[TicketAccount] = pydantic.Field(default=None)
    """
    The account associated with the ticket.
    """

    contact: typing.Optional[TicketContact] = pydantic.Field(default=None)
    """
    The contact associated with the ticket.
    """

    parent_ticket: typing.Optional["TicketParentTicket"] = pydantic.Field(default=None)
    """
    The ticket's parent ticket.
    """

    attachments: typing.Optional[typing.List[typing.Optional["TicketAttachmentsItem"]]] = None
    tags: typing.Optional[typing.List[typing.Optional[str]]] = None
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's ticket was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's ticket was updated.
    """

    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the ticket was completed.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    ticket_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 3rd party url of the Ticket.
    """

    priority: typing.Optional[TicketPriority] = pydantic.Field(default=None)
    """
    The priority or urgency of the Ticket.
    
    - `URGENT` - URGENT
    - `HIGH` - HIGH
    - `NORMAL` - NORMAL
    - `LOW` - LOW
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_data: typing.Optional[typing.List[RemoteData]] = None
    remote_fields: typing.Optional[typing.List[RemoteField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .attachment import Attachment  # noqa: E402
from .ticket_parent_ticket import TicketParentTicket  # noqa: E402
from .ticket_attachments_item import TicketAttachmentsItem  # noqa: E402

update_forward_refs(Collection, Ticket=Ticket)
update_forward_refs(Attachment, Ticket=Ticket)
update_forward_refs(Ticket)

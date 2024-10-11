# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .collection import Collection
import typing
import pydantic
import datetime as dt
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class Attachment(UniversalBaseModel):
    """
    # The Attachment Object

    ### Description

    The `Attachment` object is used to represent an attachment for a ticket.

    ### Usage Example

    TODO
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    file_name: typing.Optional[str] = pydantic.Field()
    """
    The attachment's name. It is required to include the file extension in the attachment's name.
    """

    ticket: typing.Optional["AttachmentTicket"] = pydantic.Field()
    """
    The ticket associated with the attachment.
    """

    file_url: typing.Optional[str] = pydantic.Field()
    """
    The attachment's url. It is required to include the file extension in the file's URL.
    """

    content_type: typing.Optional[str] = pydantic.Field()
    """
    The attachment's file format.
    """

    uploaded_by: typing.Optional[str] = pydantic.Field()
    """
    The user who uploaded the attachment.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's attachment was created.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .ticket import Ticket  # noqa: E402
from .attachment_ticket import AttachmentTicket  # noqa: E402

update_forward_refs(Collection, Attachment=Attachment)
update_forward_refs(Ticket, Attachment=Attachment)
update_forward_refs(Attachment)

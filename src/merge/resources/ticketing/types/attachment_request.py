# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .attachment_request_ticket import AttachmentRequestTicket


class AttachmentRequest(pydantic_v1.BaseModel):
    """
    # The Attachment Object

    ### Description

    The `Attachment` object is used to represent an attachment for a ticket.

    ### Usage Example

    TODO
    """

    file_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The attachment's name. It is required to include the file extension in the attachment's name.
    """

    ticket: typing.Optional[AttachmentRequestTicket] = pydantic_v1.Field()
    """
    The ticket associated with the attachment.
    """

    file_url: typing.Optional[str] = pydantic_v1.Field()
    """
    The attachment's url. It is required to include the file extension in the file's URL.
    """

    content_type: typing.Optional[str] = pydantic_v1.Field()
    """
    The attachment's file format.
    """

    uploaded_by: typing.Optional[str] = pydantic_v1.Field()
    """
    The user who uploaded the attachment.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}

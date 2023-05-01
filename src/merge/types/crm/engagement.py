# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Engagement", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class Engagement(BaseModel):
    account: Optional[str]
    """The account of the engagement."""

    contacts: Optional[List[Optional[str]]]

    content: Optional[str]
    """The engagement's content."""

    direction: Optional[Literal["INBOUND", "OUTBOUND"]]
    """
    - `INBOUND` - INBOUND
    - `OUTBOUND` - OUTBOUND
    """

    end_time: Optional[datetime]
    """The time at which the engagement ended."""

    engagement_type: Optional[str]
    """The engagement type of the engagement."""

    field_mappings: Optional[object]

    id: Optional[str]

    owner: Optional[str]
    """The engagement's owner."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    start_time: Optional[datetime]
    """The time at which the engagement started."""

    subject: Optional[str]
    """The engagement's subject."""

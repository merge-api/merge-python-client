# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Automation"]


class Automation(BaseModel):
    actions: List[str]
    """The actions performed by this automation."""

    automation_trigger: Optional[object]
    """The trigger configuraton for the automation."""

    description: Optional[str]
    """The automation’s description."""

    end_date: Optional[datetime]
    """The automation's end date."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The automation's name."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    start_date: Optional[datetime]
    """The automation's start date."""

    status: Optional[str]
    """The automation's status."""

    trigger_type: Optional[Literal["TRIGGER_EVENT", "RECURRENCE"]]
    """
    - `TRIGGER_EVENT` - TRIGGER_EVENT
    - `RECURRENCE` - RECURRENCE
    """

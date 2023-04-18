# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AutomationCreateParams", "Model"]


class Model(TypedDict, total=False):
    actions: Required[List[str]]
    """The actions performed by this automation."""

    automation_trigger: Optional[object]
    """The trigger configuraton for the automation."""

    description: Optional[str]
    """The automation’s description."""

    end_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The automation's end date."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The automation's name."""

    start_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The automation's start date."""

    status: Optional[str]
    """The automation's status."""

    trigger_type: Literal["TRIGGER_EVENT", "RECURRENCE"]
    """
    - `TRIGGER_EVENT` - TRIGGER_EVENT
    - `RECURRENCE` - RECURRENCE
    """


class AutomationCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Automation Object

    ### Description

    The `Automation` object is used to represent an automation, workflow or custom
    event in the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/automations` endpoint and view their
    automation_trigger configurations.
    """

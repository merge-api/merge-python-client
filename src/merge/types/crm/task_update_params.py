# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskUpdateParams", "Model"]


class Model(TypedDict, total=False):
    account: Optional[str]
    """The task's account."""

    completed_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the task is completed."""

    content: Optional[str]
    """The task's content."""

    due_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the task is due."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    owner: Optional[str]
    """The task's owner."""

    status: Literal["OPEN", "CLOSED"]
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    """

    subject: Optional[str]
    """The task's subject."""


class TaskUpdateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Task Object

    ### Description

    The `Task` object is used to represent a task, such as a to-do item.

    ### Usage Example

    TODO
    """

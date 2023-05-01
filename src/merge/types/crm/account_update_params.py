# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountUpdateParams", "Model"]


class Model(TypedDict, total=False):
    description: Optional[str]
    """The account's description."""

    industry: Optional[str]
    """The account's industry."""

    integration_params: Optional[object]

    last_activity_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    The last date (either most recent or furthest in the future) of when an activity
    occurs in an account.
    """

    linked_account_params: Optional[object]

    name: Optional[str]
    """The account's name."""

    number_of_employees: Optional[int]
    """The account's number of employees."""

    owner: Optional[str]
    """The account's owner."""

    website: Optional[str]
    """The account's website."""


class AccountUpdateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Account Object

    ### Description

    The `Account` object is used to represent a company in a CRM system.

    ### Usage Example

    TODO
    """

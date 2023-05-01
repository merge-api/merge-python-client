# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionCreateParams", "Model"]


class Model(TypedDict, total=False):
    emails: Required[List[str]]
    """The marketing emails sent by this action."""

    messages: Required[List[str]]
    """The messages sent by this action."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The action's name."""

    type: Literal["EMAIL", "MESSAGE"]
    """
    - `EMAIL` - EMAIL
    - `MESSAGE` - MESSAGE
    """


class ActionCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Action Object

    ### Description

    The `Action` object is used to represent an action executed within an
    automation.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/actions` endpoint and view their types.
    """

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActivityCreateParams", "Model"]


class Model(TypedDict, total=False):
    activity_type: Literal["CALL", "MEETING", "EMAIL"]
    """
    - `CALL` - CALL
    - `MEETING` - MEETING
    - `EMAIL` - EMAIL
    """

    body: Optional[str]
    """The activity's body."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    subject: Optional[str]
    """The activity's subject."""

    user: Optional[str]
    """The user the performed the action."""

    visibility: Literal["ADMIN_ONLY", "PUBLIC", "PRIVATE"]
    """
    - `ADMIN_ONLY` - ADMIN_ONLY
    - `PUBLIC` - PUBLIC
    - `PRIVATE` - PRIVATE
    """


class ActivityCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Activity Object

    ### Description

    The `Activity` object is used to represent an activity for a candidate performed
    by a user.

    ### Usage Example

    Fetch from the `LIST Activities` endpoint and filter by `ID` to show all
    activities.
    """

    remote_user_id: Required[str]

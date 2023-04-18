# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RemoteUser"]


class RemoteUser(TypedDict, total=False):
    access_role: Literal["SUPER_ADMIN", "ADMIN", "TEAM_MEMBER", "LIMITED_TEAM_MEMBER", "INTERVIEWER"]
    """
    - `SUPER_ADMIN` - SUPER_ADMIN
    - `ADMIN` - ADMIN
    - `TEAM_MEMBER` - TEAM_MEMBER
    - `LIMITED_TEAM_MEMBER` - LIMITED_TEAM_MEMBER
    - `INTERVIEWER` - INTERVIEWER
    """

    disabled: Optional[bool]
    """Whether the user's account had been disabled."""

    email: Optional[str]
    """The user's email."""

    first_name: Optional[str]
    """The user's first name."""

    last_name: Optional[str]
    """The user's last name."""

    remote_created_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the third party's user was created."""

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

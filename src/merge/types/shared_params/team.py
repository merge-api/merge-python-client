# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Team"]


class Team(TypedDict, total=False):
    description: Optional[str]
    """The team's description."""

    name: Optional[str]
    """The team's name."""

    parent_team: Optional[str]
    """The team's parent team."""

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

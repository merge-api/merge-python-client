# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["Issue"]


class Issue(TypedDict, total=False):
    error_description: Required[str]

    first_incident_time: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]

    last_incident_time: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]

    status: Literal["ONGOING", "RESOLVED"]
    """
    - `ONGOING` - ONGOING
    - `RESOLVED` - RESOLVED
    """

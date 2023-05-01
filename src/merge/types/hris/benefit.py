# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["Benefit"]


class Benefit(BaseModel):
    benefit_plan_type: Optional[str]
    """The type of benefit plan"""

    company_contribution: Optional[float]
    """The company's contribution."""

    employee: Optional[str]
    """The employee on the plan."""

    employee_contribution: Optional[float]
    """The employee's contribution."""

    field_mappings: Optional[object]

    id: Optional[str]

    provider_name: Optional[str]
    """The name of the benefit provider."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

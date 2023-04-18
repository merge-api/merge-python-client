# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.hris import employee

__all__ = ["CreatedEmployeeResponse"]


class CreatedEmployeeResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: employee.Employee
    """# The Employee Object

    ### Description

    The `Employee` object is used to represent any person who has been employed by a
    company.

    ### Usage Example

    Fetch from the `LIST Employee` endpoint and filter by `ID` to show all
    employees.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

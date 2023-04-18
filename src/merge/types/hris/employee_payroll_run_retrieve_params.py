# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EmployeePayrollRunRetrieveParams"]


class EmployeePayrollRunRetrieveParams(TypedDict, total=False):
    expand: List[Literal["employee", "payroll_run"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

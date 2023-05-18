# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["EmployeePayrollRun", "Earning", "Deduction", "Tax"]


class Earning(BaseModel):
    amount: Optional[float]
    """The amount earned."""

    employee_payroll_run: Optional[str]

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    type: Optional[Literal["SALARY", "REIMBURSEMENT", "OVERTIME", "BONUS"]]
    """
    - `SALARY` - SALARY
    - `REIMBURSEMENT` - REIMBURSEMENT
    - `OVERTIME` - OVERTIME
    - `BONUS` - BONUS
    """


class Deduction(BaseModel):
    company_deduction: Optional[float]
    """The amount of money that is withheld on behalf of an employee by the company."""

    employee_deduction: Optional[float]
    """
    The amount of money that is withheld from an employee's gross pay by the
    employee.
    """

    employee_payroll_run: Optional[str]

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    name: Optional[str]
    """The deduction's name."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""


class Tax(BaseModel):
    amount: Optional[float]
    """The tax amount."""

    employee_payroll_run: Optional[str]

    employer_tax: Optional[bool]
    """Whether or not the employer is responsible for paying the tax."""

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    name: Optional[str]
    """The tax's name."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""


class EmployeePayrollRun(BaseModel):
    check_date: Optional[datetime]
    """The day and time the payroll run was checked."""

    deductions: Optional[List[Deduction]]

    earnings: Optional[List[Earning]]

    employee: Optional[str]
    """The employee whose payroll is being run."""

    end_date: Optional[datetime]
    """The day and time the payroll run ended."""

    field_mappings: Optional[object]

    gross_pay: Optional[float]
    """
    The total earnings throughout a given period for an employee before any
    deductions are made.
    """

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    net_pay: Optional[float]
    """
    The take-home pay throughout a given period for an employee after deductions are
    made.
    """

    payroll_run: Optional[str]
    """The payroll being run."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    start_date: Optional[datetime]
    """The day and time the payroll run started."""

    taxes: Optional[List[Tax]]

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmployeeCreateParams", "Model"]


class Model(TypedDict, total=False):
    avatar: Optional[str]
    """The URL of the employee's avatar image."""

    company: Optional[str]
    """The ID of the employee's company."""

    date_of_birth: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The employee's date of birth."""

    display_full_name: Optional[str]
    """The employee's full name, to use for display purposes.

    If a preferred first name is available, the full name will include the preferred
    first name.
    """

    employee_number: Optional[str]
    """The employee's number that appears in the third-party integration's UI."""

    employment_status: Literal["ACTIVE", "PENDING", "INACTIVE"]
    """
    - `ACTIVE` - ACTIVE
    - `PENDING` - PENDING
    - `INACTIVE` - INACTIVE
    """

    employments: List[Optional[str]]
    """Array of `Employment` IDs for this Employee."""

    ethnicity: Literal[
        "AMERICAN_INDIAN_OR_ALASKA_NATIVE",
        "ASIAN_OR_INDIAN_SUBCONTINENT",
        "BLACK_OR_AFRICAN_AMERICAN",
        "HISPANIC_OR_LATINO",
        "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER",
        "TWO_OR_MORE_RACES",
        "WHITE",
        "PREFER_NOT_TO_DISCLOSE",
    ]
    """
    - `AMERICAN_INDIAN_OR_ALASKA_NATIVE` - AMERICAN_INDIAN_OR_ALASKA_NATIVE
    - `ASIAN_OR_INDIAN_SUBCONTINENT` - ASIAN_OR_INDIAN_SUBCONTINENT
    - `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN
    - `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO
    - `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` -
      NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER
    - `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES
    - `WHITE` - WHITE
    - `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE
    """

    first_name: Optional[str]
    """The employee's first name."""

    gender: Literal["MALE", "FEMALE", "NON-BINARY", "OTHER", "DECLINE_TO_SELF_IDENTIFY"]
    """
    - `MALE` - MALE
    - `FEMALE` - FEMALE
    - `NON-BINARY` - NON-BINARY
    - `OTHER` - OTHER
    - `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY
    """

    groups: List[Optional[str]]

    hire_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    The date that the employee was hired, usually the day that an offer letter is
    signed. If an employee has multiple hire dates from previous employments, this
    represents the most recent hire date. Note: If you're looking for the employee's
    start date, refer to the start_date field.
    """

    home_location: Optional[str]
    """The employee's home address."""

    integration_params: Optional[object]

    last_name: Optional[str]
    """The employee's last name."""

    linked_account_params: Optional[object]

    manager: Optional[str]
    """The employee ID of the employee's manager."""

    marital_status: Literal[
        "SINGLE",
        "MARRIED_FILING_JOINTLY",
        "MARRIED_FILING_SEPARATELY",
        "HEAD_OF_HOUSEHOLD",
        "QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD",
    ]
    """
    - `SINGLE` - SINGLE
    - `MARRIED_FILING_JOINTLY` - MARRIED_FILING_JOINTLY
    - `MARRIED_FILING_SEPARATELY` - MARRIED_FILING_SEPARATELY
    - `HEAD_OF_HOUSEHOLD` - HEAD_OF_HOUSEHOLD
    - `QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD` -
      QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD
    """

    mobile_phone_number: Optional[str]
    """The employee's mobile phone number."""

    pay_group: Optional[str]
    """The employee's pay group"""

    personal_email: Optional[str]
    """The employee's personal email."""

    ssn: Optional[str]
    """The employee's social security number."""

    start_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The date that the employee started working.

    If an employee was rehired, the most recent start date will be returned.
    """

    team: Optional[str]
    """The employee's team."""

    termination_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The employee's termination date."""

    username: Optional[str]
    """The employee's username that appears in the remote UI."""

    work_email: Optional[str]
    """The employee's work email."""

    work_location: Optional[str]
    """The employee's work address."""


class EmployeeCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Employee Object

    ### Description

    The `Employee` object is used to represent any person who has been employed by a
    company.

    ### Usage Example

    Fetch from the `LIST Employee` endpoint and filter by `ID` to show all
    employees.
    """

# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Employee"]


class Employee(BaseModel):
    avatar: Optional[str]
    """The URL of the employee's avatar image."""

    company: Optional[str]
    """The ID of the employee's company."""

    custom_fields: Optional[object]
    """Custom fields configured for a given model."""

    date_of_birth: Optional[datetime]
    """The employee's date of birth."""

    display_full_name: Optional[str]
    """The employee's full name, to use for display purposes.

    If a preferred first name is available, the full name will include the preferred
    first name.
    """

    employee_number: Optional[str]
    """The employee's number that appears in the third-party integration's UI."""

    employment_status: Optional[Literal["ACTIVE", "PENDING", "INACTIVE"]]
    """
    - `ACTIVE` - ACTIVE
    - `PENDING` - PENDING
    - `INACTIVE` - INACTIVE
    """

    employments: Optional[List[Optional[str]]]
    """Array of `Employment` IDs for this Employee."""

    ethnicity: Optional[
        Literal[
            "AMERICAN_INDIAN_OR_ALASKA_NATIVE",
            "ASIAN_OR_INDIAN_SUBCONTINENT",
            "BLACK_OR_AFRICAN_AMERICAN",
            "HISPANIC_OR_LATINO",
            "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER",
            "TWO_OR_MORE_RACES",
            "WHITE",
            "PREFER_NOT_TO_DISCLOSE",
        ]
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

    field_mappings: Optional[object]

    first_name: Optional[str]
    """The employee's first name."""

    gender: Optional[Literal["MALE", "FEMALE", "NON-BINARY", "OTHER", "DECLINE_TO_SELF_IDENTIFY"]]
    """
    - `MALE` - MALE
    - `FEMALE` - FEMALE
    - `NON-BINARY` - NON-BINARY
    - `OTHER` - OTHER
    - `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY
    """

    groups: Optional[List[Optional[str]]]

    hire_date: Optional[datetime]
    """
    The date that the employee was hired, usually the day that an offer letter is
    signed. If an employee has multiple hire dates from previous employments, this
    represents the most recent hire date. Note: If you're looking for the employee's
    start date, refer to the start_date field.
    """

    home_location: Optional[str]
    """The employee's home address."""

    id: Optional[str]

    last_name: Optional[str]
    """The employee's last name."""

    manager: Optional[str]
    """The employee ID of the employee's manager."""

    marital_status: Optional[
        Literal[
            "SINGLE",
            "MARRIED_FILING_JOINTLY",
            "MARRIED_FILING_SEPARATELY",
            "HEAD_OF_HOUSEHOLD",
            "QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD",
        ]
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

    remote_created_at: Optional[datetime]
    """When the third party's employee was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]

    ssn: Optional[str]
    """The employee's social security number."""

    start_date: Optional[datetime]
    """The date that the employee started working.

    If an employee was rehired, the most recent start date will be returned.
    """

    team: Optional[str]
    """The employee's team."""

    termination_date: Optional[datetime]
    """The employee's termination date."""

    username: Optional[str]
    """The employee's username that appears in the remote UI."""

    work_email: Optional[str]
    """The employee's work email."""

    work_location: Optional[str]
    """The employee's work address."""

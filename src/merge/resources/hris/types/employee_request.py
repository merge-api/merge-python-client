# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .employee import Employee
from .employment import Employment
from .team import Team
import typing
import pydantic
from .employee_request_company import EmployeeRequestCompany
from .employee_request_groups_item import EmployeeRequestGroupsItem
from .employee_request_employments_item import EmployeeRequestEmploymentsItem
from .employee_request_home_location import EmployeeRequestHomeLocation
from .employee_request_work_location import EmployeeRequestWorkLocation
from .employee_request_manager import EmployeeRequestManager
from .employee_request_team import EmployeeRequestTeam
from .employee_request_pay_group import EmployeeRequestPayGroup
from .employee_request_gender import EmployeeRequestGender
from .employee_request_ethnicity import EmployeeRequestEthnicity
from .employee_request_marital_status import EmployeeRequestMaritalStatus
import datetime as dt
from .employee_request_employment_status import EmployeeRequestEmploymentStatus
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class EmployeeRequest(UniversalBaseModel):
    """
    # The Employee Object

    ### Description

    The `Employee` object is used to represent any person who has been employed by a company.

    ### Usage Example

    Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.
    """

    employee_number: typing.Optional[str] = pydantic.Field()
    """
    The employee's number that appears in the third-party integration's UI.
    """

    company: typing.Optional[EmployeeRequestCompany] = pydantic.Field()
    """
    The ID of the employee's company.
    """

    first_name: typing.Optional[str] = pydantic.Field()
    """
    The employee's first name.
    """

    last_name: typing.Optional[str] = pydantic.Field()
    """
    The employee's last name.
    """

    preferred_name: typing.Optional[str] = pydantic.Field()
    """
    The employee's preferred first name.
    """

    display_full_name: typing.Optional[str] = pydantic.Field()
    """
    The employee's full name, to use for display purposes. If a preferred first name is available, the full name will include the preferred first name.
    """

    username: typing.Optional[str] = pydantic.Field()
    """
    The employee's username that appears in the remote UI.
    """

    groups: typing.Optional[typing.List[typing.Optional[EmployeeRequestGroupsItem]]]
    work_email: typing.Optional[str] = pydantic.Field()
    """
    The employee's work email.
    """

    personal_email: typing.Optional[str] = pydantic.Field()
    """
    The employee's personal email.
    """

    mobile_phone_number: typing.Optional[str] = pydantic.Field()
    """
    The employee's mobile phone number.
    """

    employments: typing.Optional[typing.List[typing.Optional[EmployeeRequestEmploymentsItem]]] = pydantic.Field()
    """
    Array of `Employment` IDs for this Employee.
    """

    home_location: typing.Optional[EmployeeRequestHomeLocation] = pydantic.Field()
    """
    The employee's home address.
    """

    work_location: typing.Optional[EmployeeRequestWorkLocation] = pydantic.Field()
    """
    The employee's work address.
    """

    manager: typing.Optional[EmployeeRequestManager] = pydantic.Field()
    """
    The employee ID of the employee's manager.
    """

    team: typing.Optional[EmployeeRequestTeam] = pydantic.Field()
    """
    The employee's team.
    """

    pay_group: typing.Optional[EmployeeRequestPayGroup] = pydantic.Field()
    """
    The employee's pay group
    """

    ssn: typing.Optional[str] = pydantic.Field()
    """
    The employee's social security number.
    """

    gender: typing.Optional[EmployeeRequestGender] = pydantic.Field()
    """
    The employee's gender.
    
    - `MALE` - MALE
    - `FEMALE` - FEMALE
    - `NON-BINARY` - NON-BINARY
    - `OTHER` - OTHER
    - `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE
    """

    ethnicity: typing.Optional[EmployeeRequestEthnicity] = pydantic.Field()
    """
    The employee's ethnicity.
    
    - `AMERICAN_INDIAN_OR_ALASKA_NATIVE` - AMERICAN_INDIAN_OR_ALASKA_NATIVE
    - `ASIAN_OR_INDIAN_SUBCONTINENT` - ASIAN_OR_INDIAN_SUBCONTINENT
    - `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN
    - `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO
    - `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER
    - `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES
    - `WHITE` - WHITE
    - `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE
    """

    marital_status: typing.Optional[EmployeeRequestMaritalStatus] = pydantic.Field()
    """
    The employee's filing status as related to marital status.
    
    - `SINGLE` - SINGLE
    - `MARRIED_FILING_JOINTLY` - MARRIED_FILING_JOINTLY
    - `MARRIED_FILING_SEPARATELY` - MARRIED_FILING_SEPARATELY
    - `HEAD_OF_HOUSEHOLD` - HEAD_OF_HOUSEHOLD
    - `QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD` - QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD
    """

    date_of_birth: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The employee's date of birth.
    """

    hire_date: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The date that the employee was hired, usually the day that an offer letter is signed. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. Note: If you're looking for the employee's start date, refer to the start_date field.
    """

    start_date: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The date that the employee started working. If an employee was rehired, the most recent start date will be returned.
    """

    employment_status: typing.Optional[EmployeeRequestEmploymentStatus] = pydantic.Field()
    """
    The employment status of the employee.
    
    - `ACTIVE` - ACTIVE
    - `PENDING` - PENDING
    - `INACTIVE` - INACTIVE
    """

    termination_date: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The employee's termination date.
    """

    avatar: typing.Optional[str] = pydantic.Field()
    """
    The URL of the employee's avatar image.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Employee, EmployeeRequest=EmployeeRequest)
update_forward_refs(Employment, EmployeeRequest=EmployeeRequest)
update_forward_refs(Team, EmployeeRequest=EmployeeRequest)

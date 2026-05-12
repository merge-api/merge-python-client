import os
import pytest
from merge import Merge
from merge.resources.hris.resources.employees.types.employees_list_request_expand import EmployeesListRequestExpand
from merge.resources.hris.resources.employees.types.employees_retrieve_request_expand import EmployeesRetrieveRequestExpand
from merge.resources.hris.resources.employments.types.employments_list_request_expand import EmploymentsListRequestExpand
from merge.resources.hris.resources.employments.types.employments_retrieve_request_expand import EmploymentsRetrieveRequestExpand


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_HRIS_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
        account_token=account_token,
        api_key=api_key,
    )


def test_account_details_retrieve(client):
    account_details = client.hris.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')


def test_employees_list(client):
    response = client.hris.employees.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_employees_retrieve(client):
    employees_response = client.hris.employees.list(page_size=1)

    if employees_response.results:
        employee_id = employees_response.results[0].id
        employee = client.hris.employees.retrieve(id=employee_id)
        assert employee is not None
        assert employee.id == employee_id


def test_employments_list(client):
    response = client.hris.employments.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_employments_retrieve(client):
    employments_response = client.hris.employments.list(page_size=1)

    if employments_response.results:
        employment_id = employments_response.results[0].id
        employment = client.hris.employments.retrieve(id=employment_id)
        assert employment is not None
        assert employment.id == employment_id


def test_teams_list(client):
    response = client.hris.teams.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_teams_retrieve(client):
    teams_response = client.hris.teams.list(page_size=1)

    if teams_response.results:
        team_id = teams_response.results[0].id
        team = client.hris.teams.retrieve(id=team_id)
        assert team is not None
        assert team.id == team_id


def test_locations_list(client):
    response = client.hris.locations.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_locations_retrieve(client):
    locations_response = client.hris.locations.list(page_size=1)

    if locations_response.results:
        location_id = locations_response.results[0].id
        location = client.hris.locations.retrieve(id=location_id)
        assert location is not None
        assert location.id == location_id


def test_benefits_list(client):
    response = client.hris.benefits.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_benefits_retrieve(client):
    benefits_response = client.hris.benefits.list(page_size=1)

    if benefits_response.results:
        benefit_id = benefits_response.results[0].id
        benefit = client.hris.benefits.retrieve(id=benefit_id)
        assert benefit is not None
        assert benefit.id == benefit_id


def test_pay_groups_list(client):
    response = client.hris.pay_groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_pay_groups_retrieve(client):
    pay_groups_response = client.hris.pay_groups.list(page_size=1)

    if pay_groups_response.results:
        pay_group_id = pay_groups_response.results[0].id
        pay_group = client.hris.pay_groups.retrieve(id=pay_group_id)
        assert pay_group is not None
        assert pay_group.id == pay_group_id


def test_dependents_list(client):
    response = client.hris.dependents.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_dependents_retrieve(client):
    dependents_response = client.hris.dependents.list(page_size=1)

    if dependents_response.results:
        dependent_id = dependents_response.results[0].id
        dependent = client.hris.dependents.retrieve(id=dependent_id)
        assert dependent is not None
        assert dependent.id == dependent_id


def test_groups_list(client):
    response = client.hris.groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_groups_retrieve(client):
    groups_response = client.hris.groups.list(page_size=1)

    if groups_response.results:
        group_id = groups_response.results[0].id
        group = client.hris.groups.retrieve(id=group_id)
        assert group is not None
        assert group.id == group_id


def test_time_off_list(client):
    response = client.hris.time_off.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_time_off_retrieve(client):
    time_off_response = client.hris.time_off.list(page_size=1)

    if time_off_response.results:
        time_off_id = time_off_response.results[0].id
        time_off = client.hris.time_off.retrieve(id=time_off_id)
        assert time_off is not None
        assert time_off.id == time_off_id


def test_time_off_balances_list(client):
    response = client.hris.time_off_balances.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_time_off_balances_retrieve(client):
    time_off_balances_response = client.hris.time_off_balances.list(page_size=1)

    if time_off_balances_response.results:
        time_off_balance_id = time_off_balances_response.results[0].id
        time_off_balance = client.hris.time_off_balances.retrieve(id=time_off_balance_id)
        assert time_off_balance is not None
        assert time_off_balance.id == time_off_balance_id


def test_bank_info_list(client):
    response = client.hris.bank_info.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_bank_info_retrieve(client):
    bank_info_response = client.hris.bank_info.list(page_size=1)

    if bank_info_response.results:
        bank_info_id = bank_info_response.results[0].id
        bank_info = client.hris.bank_info.retrieve(id=bank_info_id)
        assert bank_info is not None
        assert bank_info.id == bank_info_id


def test_employees_list_with_expand_company(client):
    response = client.hris.employees.list(expand=EmployeesListRequestExpand.COMPANY)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_employees_retrieve_with_expand_employments(client):
    employees_response = client.hris.employees.list(page_size=1)

    if employees_response.results:
        employee_id = employees_response.results[0].id
        employee = client.hris.employees.retrieve(id=employee_id, expand=EmployeesRetrieveRequestExpand.EMPLOYMENTS)
        assert employee is not None
        assert employee.id == employee_id


def test_employments_list_with_expand_employee(client):
    response = client.hris.employments.list(expand=EmploymentsListRequestExpand.EMPLOYEE)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_employments_retrieve_with_expand_pay_group(client):
    employments_response = client.hris.employments.list(page_size=1)

    if employments_response.results:
        employment_id = employments_response.results[0].id
        employment = client.hris.employments.retrieve(id=employment_id, expand=EmploymentsRetrieveRequestExpand.PAY_GROUP)
        assert employment is not None
        assert employment.id == employment_id


def test_employees_list_with_expand_string(client):
    response = client.hris.employees.list(expand="company")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_employments_list_with_expand_string(client):
    response = client.hris.employments.list(expand="employee")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)



import os
import pytest
from typing import Optional

from merge.resources.ats.client import AtsClient
from merge.resources.ats.types.categories_enum import CategoriesEnum
from merge.resources.hris.client import HrisClient
from merge.core.api_error import ApiError
from merge.client import Merge
from merge.environment import MergeEnvironment


def test_unauthorized_client_error() -> None:
    client = Merge(api_key="Bearer invalid", environment=MergeEnvironment.SANDBOX)
    with pytest.raises(ApiError) as exception:
        response = client.ats.account_details.retrieve()
    assert exception.value.status_code == 401


def test_bad_request_api_key_error() -> None:
    client = Merge(api_key="invalid", environment=MergeEnvironment.SANDBOX)
    with pytest.raises(ApiError) as exception:
        response = client.ats.account_details.retrieve()
    assert exception.value.status_code == 400


def test_account_token_error(ats_client: AtsClient, hris_client: HrisClient) -> None:
    with pytest.raises(ApiError) as exception:
        ats_response = ats_client.account_token.retrieve(public_token="notfound")
    assert exception.value.status_code == 404

    with pytest.raises(ApiError) as exception:
        hris_response = hris_client.account_token.retrieve(public_token="notfound")
    assert exception.value.status_code == 404


def test_link_token(ats_client: AtsClient) -> None:
    response = ats_client.link_token.create(
        end_user_email_address="john.smith@gmail.com",
        end_user_organization_name="acme",
        end_user_origin_id="1234",
        categories=[CategoriesEnum.ATS],
        link_expiry_mins=30,
    )
    assert response is not None
    assert len(response.link_token) > 0


def test_employees(hris_client: HrisClient) -> None:
    response = hris_client.employees.list()
    assert response is not None
    assert response.results is not None
    assert len(response.results) > 0

    for i, employee in enumerate(response.results):
        assert employee.id is not None
        retrieved = hris_client.employees.retrieve(id=employee.id)
        assert retrieved.id == employee.id

    response = hris_client.employees.list(created_after="2030-01-01")
    assert response is not None
    assert response.results is not None
    assert len(response.results) == 0


def test_candidates(ats_client: AtsClient) -> None:
    response = ats_client.candidates.list()
    assert response is not None
    assert response.results is not None
    assert len(response.results) > 0

    for i, candidate in enumerate(response.results):
        assert candidate.id is not None
        retrieved = ats_client.candidates.retrieve(id=candidate.id)
        assert retrieved.id == candidate.id

    first_candidate = response.results[0]
    filtered = ats_client.candidates.list(
        first_name=first_candidate.first_name,
        last_name=first_candidate.last_name,
    )
    assert filtered is not None
    assert filtered.results is not None
    assert len(filtered.results) >= 1
    assert len(filtered.results) <= len(response.results)

    for i, candidate in enumerate(filtered.results):
        assert candidate.first_name is not None
        assert first_candidate.first_name is not None
        assert first_candidate.first_name in candidate.first_name

        assert candidate.last_name is not None
        assert first_candidate.last_name is not None
        assert first_candidate.last_name in candidate.last_name

    response = ats_client.candidates.list(created_after="2030-01-01")
    assert response is not None
    assert response.results is not None
    assert len(response.results) == 0


def test_retrieve_account_info(
    ats_client: AtsClient,
    hris_client: HrisClient,
    ats_account_id: str,
    hris_account_id: str,
) -> None:
    ats_response = ats_client.account_details.retrieve()
    assert ats_response is not None
    assert ats_response.id == ats_account_id

    hris_response = hris_client.account_details.retrieve()
    assert hris_response is not None
    assert hris_response.id == hris_account_id


@pytest.fixture
def ats_client() -> AtsClient:
    account_token = os.environ.get("TEST_MERGE_ATS_ACCOUNT_TOKEN")
    return Merge(
        api_key=get_api_key(),
        account_token=account_token,
    ).ats


@pytest.fixture
def ats_account_id() -> Optional[str]:
    return os.environ.get("TEST_MERGE_ATS_ACCOUNT_ID")


@pytest.fixture
def hris_client() -> HrisClient:
    account_token = os.environ.get("TEST_MERGE_HRIS_ACCOUNT_TOKEN")
    return Merge(
        api_key=get_api_key(),
        account_token=account_token,
    ).hris


@pytest.fixture
def hris_account_id() -> Optional[str]:
    return os.environ.get("TEST_MERGE_HRIS_ACCOUNT_ID")


def get_api_key() -> str:
    """
    Returns the API key required to call the Merge API.

    We don't want this to be a fixture because it would otherwise
    be visible in the console.
    """
    api_key = os.environ.get("TEST_MERGE_API_KEY")
    if api_key is None: 
        raise Exception("TEST_MERGE_API_KEY not found")
    return api_key

import os
import pytest
from merge import Merge
from merge.resources.crm.resources.contacts.types.contacts_list_request_expand import ContactsListRequestExpand
from merge.resources.crm.resources.contacts.types.contacts_retrieve_request_expand import ContactsRetrieveRequestExpand
from merge.resources.crm.resources.opportunities.types.opportunities_list_request_expand import OpportunitiesListRequestExpand
from merge.resources.crm.resources.opportunities.types.opportunities_retrieve_request_expand import OpportunitiesRetrieveRequestExpand


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_CRM_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
        account_token=account_token,
        api_key=api_key,
    )


def test_account_details_retrieve(client):
    account_details = client.crm.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')


def test_accounts_list(client):
    response = client.crm.accounts.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_accounts_retrieve(client):
    accounts_response = client.crm.accounts.list(page_size=1)

    if accounts_response.results:
        account_id = accounts_response.results[0].id
        account = client.crm.accounts.retrieve(id=account_id)
        assert account is not None
        assert account.id == account_id


def test_contacts_list(client):
    response = client.crm.contacts.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_contacts_retrieve(client):
    contacts_response = client.crm.contacts.list(page_size=1)

    if contacts_response.results:
        contact_id = contacts_response.results[0].id
        contact = client.crm.contacts.retrieve(id=contact_id)
        assert contact is not None
        assert contact.id == contact_id


def test_leads_list(client):
    response = client.crm.leads.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_leads_retrieve(client):
    leads_response = client.crm.leads.list(page_size=1)

    if leads_response.results:
        lead_id = leads_response.results[0].id
        lead = client.crm.leads.retrieve(id=lead_id)
        assert lead is not None
        assert lead.id == lead_id


def test_opportunities_list(client):
    response = client.crm.opportunities.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_opportunities_retrieve(client):
    opportunities_response = client.crm.opportunities.list(page_size=1)

    if opportunities_response.results:
        opportunity_id = opportunities_response.results[0].id
        opportunity = client.crm.opportunities.retrieve(id=opportunity_id)
        assert opportunity is not None
        assert opportunity.id == opportunity_id


def test_users_list(client):
    response = client.crm.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_users_retrieve(client):
    users_response = client.crm.users.list(page_size=1)

    if users_response.results:
        user_id = users_response.results[0].id
        user = client.crm.users.retrieve(id=user_id)
        assert user is not None
        assert user.id == user_id


def test_tasks_list(client):
    response = client.crm.tasks.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_tasks_retrieve(client):
    tasks_response = client.crm.tasks.list(page_size=1)

    if tasks_response.results:
        task_id = tasks_response.results[0].id
        task = client.crm.tasks.retrieve(id=task_id)
        assert task is not None
        assert task.id == task_id


def test_notes_list(client):
    response = client.crm.notes.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_notes_retrieve(client):
    notes_response = client.crm.notes.list(page_size=1)

    if notes_response.results:
        note_id = notes_response.results[0].id
        note = client.crm.notes.retrieve(id=note_id)
        assert note is not None
        assert note.id == note_id


def test_engagements_list(client):
    response = client.crm.engagements.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_engagements_retrieve(client):
    engagements_response = client.crm.engagements.list(page_size=1)

    if engagements_response.results:
        engagement_id = engagements_response.results[0].id
        engagement = client.crm.engagements.retrieve(id=engagement_id)
        assert engagement is not None
        assert engagement.id == engagement_id


def test_stages_list(client):
    response = client.crm.stages.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_stages_retrieve(client):
    stages_response = client.crm.stages.list(page_size=1)

    if stages_response.results:
        stage_id = stages_response.results[0].id
        stage = client.crm.stages.retrieve(id=stage_id)
        assert stage is not None
        assert stage.id == stage_id


def test_custom_object_classes_list(client):
    response = client.crm.custom_object_classes.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_custom_object_classes_retrieve(client):
    custom_object_classes_response = client.crm.custom_object_classes.list(page_size=1)

    if custom_object_classes_response.results:
        custom_object_class_id = custom_object_classes_response.results[0].id
        custom_object_class = client.crm.custom_object_classes.retrieve(id=custom_object_class_id)
        assert custom_object_class is not None
        assert custom_object_class.id == custom_object_class_id


def test_contacts_list_with_expand_account(client):
    response = client.crm.contacts.list(expand=ContactsListRequestExpand.ACCOUNT)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_contacts_retrieve_with_expand_account(client):
    contacts_response = client.crm.contacts.list(page_size=1)

    if contacts_response.results:
        contact_id = contacts_response.results[0].id
        contact = client.crm.contacts.retrieve(id=contact_id, expand=ContactsRetrieveRequestExpand.ACCOUNT)
        assert contact is not None
        assert contact.id == contact_id


def test_opportunities_list_with_expand_account(client):
    response = client.crm.opportunities.list(expand=OpportunitiesListRequestExpand.ACCOUNT)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_opportunities_retrieve_with_expand_stage(client):
    opportunities_response = client.crm.opportunities.list(page_size=1)

    if opportunities_response.results:
        opportunity_id = opportunities_response.results[0].id
        opportunity = client.crm.opportunities.retrieve(id=opportunity_id, expand=OpportunitiesRetrieveRequestExpand.STAGE)
        assert opportunity is not None
        assert opportunity.id == opportunity_id


def test_contacts_list_with_expand_string(client):
    response = client.crm.contacts.list(expand="account")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_opportunities_list_with_expand_string(client):
    response = client.crm.opportunities.list(expand="stage")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)



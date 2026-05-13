import os
import pytest
from merge import Merge
from merge.resources.ticketing.resources.tickets.types.tickets_list_request_expand_item import TicketsListRequestExpandItem
from merge.resources.ticketing.resources.tickets.types.tickets_retrieve_request_expand_item import TicketsRetrieveRequestExpandItem
from merge.resources.ticketing.resources.collections.types.collections_list_request_expand_item import CollectionsListRequestExpandItem
from merge.resources.ticketing.resources.collections.types.collections_retrieve_request_expand_item import CollectionsRetrieveRequestExpandItem
from merge.resources.ticketing.resources.comments.types.comments_list_request_expand_item import CommentsListRequestExpandItem
from merge.resources.ticketing.resources.users.types.users_list_request_expand_item import UsersListRequestExpandItem


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_TICKETING_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
            account_token=account_token,
            api_key=api_key,
    )

def test_tickets_list(client):
    response = client.ticketing.tickets.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_retrieve(client):
    tickets_response = client.ticketing.tickets.list(page_size=1)

    if tickets_response.results:
        ticket_id = tickets_response.results[0].id
        ticket = client.ticketing.tickets.retrieve(id=ticket_id)
        assert ticket is not None
        assert ticket.id == ticket_id

def test_tickets_list_with_expand_assignees(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.ASSIGNEES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_list_with_expand_creator(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.CREATOR)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_list_with_expand_collections(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.COLLECTIONS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_list_with_expand_attachments(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.ATTACHMENTS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_list_with_expand_account(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.ACCOUNT)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_list_with_expand_contact(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.CONTACT)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_list_with_expand_parent_ticket(client):
    response = client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.PARENT_TICKET)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tickets_retrieve_with_expand_assignees(client):
    tickets_response = client.ticketing.tickets.list(page_size=1)

    if tickets_response.results:
        ticket_id = tickets_response.results[0].id
        ticket = client.ticketing.tickets.retrieve(id=ticket_id, expand=TicketsRetrieveRequestExpandItem.ASSIGNEES)
        assert ticket is not None
        assert ticket.id == ticket_id

def test_collections_list(client):
    response = client.ticketing.collections.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_collections_retrieve(client):
    collections_response = client.ticketing.collections.list(page_size=1)

    if collections_response.results:
        collection_id = collections_response.results[0].id
        collection = client.ticketing.collections.retrieve(id=collection_id)
        assert collection is not None
        assert collection.id == collection_id

def test_collections_list_with_expand_parent_collection(client):
    response = client.ticketing.collections.list(expand=CollectionsListRequestExpandItem.PARENT_COLLECTION)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_collections_list_with_expand_permissions(client):
    response = client.ticketing.collections.list(expand=CollectionsListRequestExpandItem.PERMISSIONS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_collections_retrieve_with_expand_parent_collection(client):
    collections_response = client.ticketing.collections.list(page_size=1)

    if collections_response.results:
        collection_id = collections_response.results[0].id
        collection = client.ticketing.collections.retrieve(id=collection_id, expand=CollectionsRetrieveRequestExpandItem.PARENT_COLLECTION)
        assert collection is not None
        assert collection.id == collection_id

def test_comments_list(client):
    response = client.ticketing.comments.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_comments_retrieve(client):
    comments_response = client.ticketing.comments.list(page_size=1)

    if comments_response.results:
        comment_id = comments_response.results[0].id
        comment = client.ticketing.comments.retrieve(id=comment_id)
        assert comment is not None
        assert comment.id == comment_id

def test_comments_list_with_expand_user(client):
    response = client.ticketing.comments.list(expand=CommentsListRequestExpandItem.USER)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_comments_list_with_expand_ticket(client):
    response = client.ticketing.comments.list(expand=CommentsListRequestExpandItem.TICKET)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_comments_list_with_expand_contact(client):
    response = client.ticketing.comments.list(expand=CommentsListRequestExpandItem.CONTACT)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_projects_list(client):
    response = client.ticketing.projects.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_projects_retrieve(client):
    projects_response = client.ticketing.projects.list(page_size=1)

    if projects_response.results:
        project_id = projects_response.results[0].id
        project = client.ticketing.projects.retrieve(id=project_id)
        assert project is not None
        assert project.id == project_id

def test_contacts_list(client):
    response = client.ticketing.contacts.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_contacts_retrieve(client):
    contacts_response = client.ticketing.contacts.list(page_size=1)

    if contacts_response.results:
        contact_id = contacts_response.results[0].id
        contact = client.ticketing.contacts.retrieve(id=contact_id)
        assert contact is not None
        assert contact.id == contact_id

def test_users_list(client):
    response = client.ticketing.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_retrieve(client):
    users_response = client.ticketing.users.list(page_size=1)

    if users_response.results:
        user_id = users_response.results[0].id
        user = client.ticketing.users.retrieve(id=user_id)
        assert user is not None
        assert user.id == user_id

def test_users_list_with_expand_roles(client):
    response = client.ticketing.users.list(expand=UsersListRequestExpandItem.ROLES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_list_with_expand_teams(client):
    response = client.ticketing.users.list(expand=UsersListRequestExpandItem.TEAMS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_teams_list(client):
    response = client.ticketing.teams.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_teams_retrieve(client):
    teams_response = client.ticketing.teams.list(page_size=1)

    if teams_response.results:
        team_id = teams_response.results[0].id
        team = client.ticketing.teams.retrieve(id=team_id)
        assert team is not None
        assert team.id == team_id

def test_roles_list(client):
    response = client.ticketing.roles.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_roles_retrieve(client):
    roles_response = client.ticketing.roles.list(page_size=1)

    if roles_response.results:
        role_id = roles_response.results[0].id
        role = client.ticketing.roles.retrieve(id=role_id)
        assert role is not None
        assert role.id == role_id

def test_tags_list(client):
    response = client.ticketing.tags.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_tags_retrieve(client):
    tags_response = client.ticketing.tags.list(page_size=1)

    if tags_response.results:
        tag_id = tags_response.results[0].id
        tag = client.ticketing.tags.retrieve(id=tag_id)
        assert tag is not None
        assert tag.id == tag_id

def test_attachments_list(client):
    response = client.ticketing.attachments.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_attachments_retrieve(client):
    attachments_response = client.ticketing.attachments.list(page_size=1)

    if attachments_response.results:
        attachment_id = attachments_response.results[0].id
        attachment = client.ticketing.attachments.retrieve(id=attachment_id)
        assert attachment is not None
        assert attachment.id == attachment_id

def test_accounts_list(client):
    response = client.ticketing.accounts.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_accounts_retrieve(client):
    accounts_response = client.ticketing.accounts.list(page_size=1)

    if accounts_response.results:
        account_id = accounts_response.results[0].id
        account = client.ticketing.accounts.retrieve(id=account_id)
        assert account is not None
        assert account.id == account_id

def test_sync_status_list(client):
    response = client.ticketing.sync_status.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_account_details_retrieve(client):
    account_details = client.ticketing.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')

def test_audit_trail_list(client):
    response = client.ticketing.audit_trail.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_available_actions_retrieve(client):
    available_actions = client.ticketing.available_actions.retrieve()

    assert available_actions is not None

def test_linked_accounts_list(client):
    response = client.ticketing.linked_accounts.list()

    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_scopes_default_scopes_retrieve(client):
    response = client.ticketing.scopes.default_scopes_retrieve()

    assert response is not None

def test_scopes_linked_account_scopes_retrieve(client):
    response = client.ticketing.scopes.linked_account_scopes_retrieve()

    assert response is not None

import os
import pytest
from merge import Merge
from merge.resources.knowledgebase.resources.articles.types.articles_list_request_expand import ArticlesListRequestExpand
from merge.resources.knowledgebase.resources.articles.types.articles_retrieve_request_expand import ArticlesRetrieveRequestExpand
from merge.resources.knowledgebase.resources.containers.types.containers_list_request_expand import ContainersListRequestExpand
from merge.resources.knowledgebase.resources.containers.types.containers_retrieve_request_expand import ContainersRetrieveRequestExpand
from merge.resources.knowledgebase.resources.groups.types.groups_list_request_expand import GroupsListRequestExpand
from merge.resources.knowledgebase.resources.groups.types.groups_retrieve_request_expand import GroupsRetrieveRequestExpand


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_KNOWLEDGEBASE_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY"]

    return Merge(
            account_token=account_token,
            api_key=api_key,
    )

def test_articles_list(client):
    response = client.knowledgebase.articles.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_articles_list_with_expand_author(client):
    response = client.knowledgebase.articles.list(expand=ArticlesListRequestExpand.AUTHOR)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_articles_list_with_expand_attachments(client):
    response = client.knowledgebase.articles.list(expand=ArticlesListRequestExpand.ATTACHMENTS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_articles_list_with_expand_permissions(client):
    response = client.knowledgebase.articles.list(expand=ArticlesListRequestExpand.PERMISSIONS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_attachments_list(client):
    response = client.knowledgebase.attachments.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_attachments_retrieve(client):
    attachments_response = client.knowledgebase.attachments.list(page_size=1)

    if attachments_response.results:
        attachment_id = attachments_response.results[0].id
        attachment = client.knowledgebase.attachments.retrieve(id=attachment_id)
        assert attachment is not None
        assert attachment.id == attachment_id

def test_containers_list(client):
    response = client.knowledgebase.containers.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_containers_retrieve(client):
    containers_response = client.knowledgebase.containers.list(page_size=1)

    if containers_response.results:
        container_id = containers_response.results[0].id
        container = client.knowledgebase.containers.retrieve(id=container_id)
        assert container is not None
        assert container.id == container_id

def test_containers_list_with_expand_permissions(client):
    response = client.knowledgebase.containers.list(expand=ContainersListRequestExpand.PERMISSIONS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_containers_list_with_expand_parent_container(client):
    response = client.knowledgebase.containers.list(expand=ContainersListRequestExpand.PARENT_CONTAINER)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_containers_retrieve_with_expand_permissions(client):
    containers_response = client.knowledgebase.containers.list(page_size=1)

    if containers_response.results:
        container_id = containers_response.results[0].id
        container = client.knowledgebase.containers.retrieve(id=container_id, expand=ContainersRetrieveRequestExpand.PERMISSIONS)
        assert container is not None
        assert container.id == container_id

def test_containers_retrieve_with_expand_parent_container(client):
    containers_response = client.knowledgebase.containers.list(page_size=1)

    if containers_response.results:
        container_id = containers_response.results[0].id
        container = client.knowledgebase.containers.retrieve(id=container_id, expand=ContainersRetrieveRequestExpand.PARENT_CONTAINER)
        assert container is not None
        assert container.id == container_id

def test_sync_status_list(client):
    response = client.knowledgebase.sync_status.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_account_details_retrieve(client):
    account_details = client.knowledgebase.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')

def test_users_list(client):
    response = client.knowledgebase.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_retrieve(client):
    users_response = client.knowledgebase.users.list(page_size=1)

    if users_response.results:
        user_id = users_response.results[0].id
        user = client.knowledgebase.users.retrieve(id=user_id)

        assert user is not None
        assert user.id == user_id

def test_groups_list(client):
    response = client.knowledgebase.groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_list_with_expand_users(client):
    response = client.knowledgebase.groups.list(expand=GroupsListRequestExpand.USERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_list_with_expand_parent_group(client):
    response = client.knowledgebase.groups.list(expand=GroupsListRequestExpand.PARENT_GROUP)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_audit_trail_list(client):
    response = client.knowledgebase.audit_trail.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_available_actions_retrieve(client):
    available_actions = client.knowledgebase.available_actions.retrieve()

    assert available_actions is not None

def test_linked_accounts_list(client):
    response = client.knowledgebase.linked_accounts.list()

    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_scopes_default_scopes_retrieve(client):
    response = client.knowledgebase.scopes.default_scopes_retrieve()

    assert response is not None

def test_scopes_linked_account_scopes_retrieve(client):
    response = client.knowledgebase.scopes.linked_account_scopes_retrieve()

    assert response is not None
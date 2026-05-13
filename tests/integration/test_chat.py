import os
import pytest
from merge import Merge
from merge.resources.chat.resources.conversations.types.conversations_members_list_request_expand_item import ConversationsMembersListRequestExpandItem
from merge.resources.chat.resources.messages.types.messages_list_request_order_by import MessagesListRequestOrderBy
from merge.resources.chat.resources.messages.types.messages_replies_list_request_order_by import MessagesRepliesListRequestOrderBy


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_CHAT_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
            account_token=account_token,
            api_key=api_key,
    )

def test_conversations_list(client):
    response = client.chat.conversations.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_conversations_retrieve(client):
    conversations_response = client.chat.conversations.list(page_size=1)

    if conversations_response.results:
        conversation_id = conversations_response.results[0].id
        conversation = client.chat.conversations.retrieve(id=conversation_id)
        assert conversation is not None
        assert conversation.id == conversation_id

def test_conversations_retrieve_with_expand_members(client):
    conversations_response = client.chat.conversations.list(page_size=1)

    if conversations_response.results:
        conversation_id = conversations_response.results[0].id
        conversation = client.chat.conversations.retrieve(id=conversation_id, expand="members")
        assert conversation is not None
        assert conversation.id == conversation_id

def test_conversations_members_list(client):
    conversations_response = client.chat.conversations.list(page_size=1)

    if conversations_response.results:
        conversation_id = conversations_response.results[0].id
        response = client.chat.conversations.members_list(conversation_id=conversation_id)
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

def test_conversations_members_list_with_expand_user(client):
    conversations_response = client.chat.conversations.list(page_size=1)

    if conversations_response.results:
        conversation_id = conversations_response.results[0].id
        response = client.chat.conversations.members_list(
            conversation_id=conversation_id,
            expand=ConversationsMembersListRequestExpandItem.USER,
        )
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

def test_conversations_members_list_with_expand_group(client):
    conversations_response = client.chat.conversations.list(page_size=1)

    if conversations_response.results:
        conversation_id = conversations_response.results[0].id
        response = client.chat.conversations.members_list(
            conversation_id=conversation_id,
            expand=ConversationsMembersListRequestExpandItem.GROUP,
        )
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

def test_messages_list(client):
    response = client.chat.messages.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_retrieve(client):
    messages_response = client.chat.messages.list(page_size=1)

    if messages_response.results:
        message_id = messages_response.results[0].id
        message = client.chat.messages.retrieve(id=message_id)
        assert message is not None
        assert message.id == message_id

def test_messages_list_with_order_by_remote_created_at(client):
    response = client.chat.messages.list(order_by=MessagesListRequestOrderBy.REMOTE_CREATED_AT_ASCENDING)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_list_with_order_by_remote_created_at_descending(client):
    response = client.chat.messages.list(order_by=MessagesListRequestOrderBy.REMOTE_CREATED_AT_DESCENDING)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_list_with_root_message_true(client):
    response = client.chat.messages.list(root_message="true")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_replies_list(client):
    messages_response = client.chat.messages.list(page_size=1)

    if messages_response.results:
        message_id = messages_response.results[0].id
        response = client.chat.messages.replies_list(message_id=message_id)
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

def test_messages_replies_list_with_order_by(client):
    messages_response = client.chat.messages.list(page_size=1)

    if messages_response.results:
        message_id = messages_response.results[0].id
        response = client.chat.messages.replies_list(
            message_id=message_id,
            order_by=MessagesRepliesListRequestOrderBy.REMOTE_CREATED_AT_ASCENDING,
        )
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

def test_users_list(client):
    response = client.chat.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_list(client):
    response = client.chat.groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_sync_status_list(client):
    response = client.chat.sync_status.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_account_details_retrieve(client):
    account_details = client.chat.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')

def test_audit_trail_list(client):
    response = client.chat.audit_trail.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_available_actions_retrieve(client):
    available_actions = client.chat.available_actions.retrieve()

    assert available_actions is not None

def test_linked_accounts_list(client):
    response = client.chat.linked_accounts.list()

    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_scopes_default_scopes_retrieve(client):
    response = client.chat.scopes.default_scopes_retrieve()

    assert response is not None

def test_scopes_linked_account_scopes_retrieve(client):
    response = client.chat.scopes.linked_account_scopes_retrieve()

    assert response is not None

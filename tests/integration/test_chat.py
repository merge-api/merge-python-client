import os
import pytest
from merge import Merge


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_CHAT_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY"]

    return Merge(
        account_token=account_token,
        api_key=api_key,
    )


def test_account_details_retrieve(client):
    account_details = client.chat.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')


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


def test_users_list(client):
    response = client.chat.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_users_retrieve(client):
    users_response = client.chat.users.list(page_size=1)

    if users_response.results:
        user_id = users_response.results[0].id
        user = client.chat.users.retrieve(id=user_id)
        assert user is not None
        assert user.id == user_id


def test_groups_list(client):
    response = client.chat.groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_groups_retrieve(client):
    groups_response = client.chat.groups.list(page_size=1)

    if groups_response.results:
        group_id = groups_response.results[0].id
        group = client.chat.groups.retrieve(id=group_id)
        assert group is not None
        assert group.id == group_id


def test_conversations_list_with_expand_string(client):
    response = client.chat.conversations.list(expand="members")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_messages_list_with_expand_string(client):
    response = client.chat.messages.list(expand="conversation")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)



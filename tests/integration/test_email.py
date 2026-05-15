import os
import pytest
from merge import Merge
from merge.resources.email.resources.email_addresses.types.email_addresses_list_request_expand_item import EmailAddressesListRequestExpandItem
from merge.resources.email.resources.folders.types.folders_list_request_expand_item import FoldersListRequestExpandItem
from merge.resources.email.resources.groups.types.groups_list_request_expand_item import GroupsListRequestExpandItem
from merge.resources.email.resources.mailboxes.types.mailboxes_list_request_expand_item import MailboxesListRequestExpandItem
from merge.resources.email.resources.mailboxes.types.mailboxes_retrieve_request_expand_item import MailboxesRetrieveRequestExpandItem
from merge.resources.email.resources.messages.types.messages_list_request_expand_item import MessagesListRequestExpandItem
from merge.resources.email.resources.messages.types.messages_retrieve_request_expand_item import MessagesRetrieveRequestExpandItem
from merge.resources.email.resources.users.types.users_list_request_expand_item import UsersListRequestExpandItem


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_EMAIL_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
            account_token=account_token,
            api_key=api_key,
    )

def test_email_addresses_list(client):
    response = client.email.email_addresses.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_email_addresses_retrieve(client):
    email_addresses_response = client.email.email_addresses.list(page_size=1)

    if email_addresses_response.results:
        email_address_id = email_addresses_response.results[0].id
        email_address = client.email.email_addresses.retrieve(id=email_address_id)
        assert email_address is not None
        assert email_address.id == email_address_id

def test_email_addresses_list_with_expand_users(client):
    response = client.email.email_addresses.list(expand=EmailAddressesListRequestExpandItem.USERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_email_addresses_list_with_expand_groups(client):
    response = client.email.email_addresses.list(expand=EmailAddressesListRequestExpandItem.GROUPS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_folders_list(client):
    response = client.email.folders.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_folders_retrieve(client):
    folders_response = client.email.folders.list(page_size=1)

    if folders_response.results:
        folder_id = folders_response.results[0].id
        folder = client.email.folders.retrieve(id=folder_id)
        assert folder is not None
        assert folder.id == folder_id

def test_folders_list_with_expand_parent_folder(client):
    response = client.email.folders.list(expand=FoldersListRequestExpandItem.PARENT_FOLDER)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_folders_list_with_expand_permissions(client):
    response = client.email.folders.list(expand=FoldersListRequestExpandItem.PERMISSIONS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_list(client):
    response = client.email.groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_retrieve(client):
    groups_response = client.email.groups.list(page_size=1)

    if groups_response.results:
        group_id = groups_response.results[0].id
        group = client.email.groups.retrieve(id=group_id)
        assert group is not None
        assert group.id == group_id

def test_groups_list_with_expand_users(client):
    response = client.email.groups.list(expand=GroupsListRequestExpandItem.USERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_list_with_expand_email_addresses(client):
    response = client.email.groups.list(expand=GroupsListRequestExpandItem.EMAIL_ADDRESSES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_mailboxes_list(client):
    response = client.email.mailboxes.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_mailboxes_retrieve(client):
    mailboxes_response = client.email.mailboxes.list(page_size=1)

    if mailboxes_response.results:
        mailbox_id = mailboxes_response.results[0].id
        mailbox = client.email.mailboxes.retrieve(id=mailbox_id)
        assert mailbox is not None
        assert mailbox.id == mailbox_id

def test_mailboxes_list_with_expand_primary_email_address(client):
    response = client.email.mailboxes.list(expand=MailboxesListRequestExpandItem.PRIMARY_EMAIL_ADDRESS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_mailboxes_list_with_expand_folders(client):
    response = client.email.mailboxes.list(expand=MailboxesListRequestExpandItem.FOLDERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_mailboxes_list_with_expand_users(client):
    response = client.email.mailboxes.list(expand=MailboxesListRequestExpandItem.USERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_mailboxes_retrieve_with_expand_primary_email_address(client):
    mailboxes_response = client.email.mailboxes.list(page_size=1)

    if mailboxes_response.results:
        mailbox_id = mailboxes_response.results[0].id
        mailbox = client.email.mailboxes.retrieve(id=mailbox_id, expand=MailboxesRetrieveRequestExpandItem.PRIMARY_EMAIL_ADDRESS)
        assert mailbox is not None
        assert mailbox.id == mailbox_id

def test_messages_list(client):
    response = client.email.messages.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_retrieve(client):
    messages_response = client.email.messages.list(page_size=1)

    if messages_response.results:
        message_id = messages_response.results[0].id
        message = client.email.messages.retrieve(id=message_id)
        assert message is not None
        assert message.id == message_id

def test_messages_list_with_expand_from_address(client):
    response = client.email.messages.list(expand=MessagesListRequestExpandItem.FROM_ADDRESS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_list_with_expand_to(client):
    response = client.email.messages.list(expand=MessagesListRequestExpandItem.TO)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_list_with_expand_folders(client):
    response = client.email.messages.list(expand=MessagesListRequestExpandItem.FOLDERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_list_with_expand_thread(client):
    response = client.email.messages.list(expand=MessagesListRequestExpandItem.THREAD)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_messages_retrieve_with_expand_from_address(client):
    messages_response = client.email.messages.list(page_size=1)

    if messages_response.results:
        message_id = messages_response.results[0].id
        message = client.email.messages.retrieve(id=message_id, expand=MessagesRetrieveRequestExpandItem.FROM_ADDRESS)
        assert message is not None
        assert message.id == message_id

def test_users_list(client):
    response = client.email.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_retrieve(client):
    users_response = client.email.users.list(page_size=1)

    if users_response.results:
        user_id = users_response.results[0].id
        user = client.email.users.retrieve(id=user_id)

        assert user is not None
        assert user.id == user_id

def test_users_list_with_expand_email_addresses(client):
    response = client.email.users.list(expand=UsersListRequestExpandItem.EMAIL_ADDRESSES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_list_with_expand_groups(client):
    response = client.email.users.list(expand=UsersListRequestExpandItem.GROUPS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_sync_status_list(client):
    response = client.email.sync_status.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_account_details_retrieve(client):
    account_details = client.email.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')

def test_audit_trail_list(client):
    response = client.email.audit_trail.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_available_actions_retrieve(client):
    available_actions = client.email.available_actions.retrieve()

    assert available_actions is not None

def test_scopes_default_scopes_retrieve(client):
    response = client.email.scopes.default_scopes_retrieve()

    assert response is not None

def test_scopes_linked_account_scopes_retrieve(client):
    response = client.email.scopes.linked_account_scopes_retrieve()

    assert response is not None

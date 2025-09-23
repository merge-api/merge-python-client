import os

import pytest

from merge import Merge
from merge.resources.filestorage.types.permission import Permission


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_FILE_STORAGE_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY"]
    
    return Merge(
            account_token=account_token,
            api_key=api_key,
    )

def test_files_list(client):
    response = client.filestorage.files.list()    
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_files_list_permissions(client):
    
    response = client.filestorage.files.list(page_size=1)
    assert response.results
    file = response.results[0]
    first_permission = file.permissions[0]

    assert isinstance(first_permission, Permission), type(first_permission)

def test_files_retrieve(client):
    files_response = client.filestorage.files.list(page_size=1)
    
    assert files_response.results, "No files available to test retrieve"
        
    file_id = files_response.results[0].id
    file = client.filestorage.files.retrieve(id=file_id)
        
    assert file is not None
    assert file.id == file_id

def test_sync_status_list(client):
    response = client.filestorage.sync_status.list()    
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_account_details_retrieve(client):
    account_details = client.filestorage.account_details.retrieve()    
    assert account_details is not None
    assert hasattr(account_details, 'id')

def test_drives_list(client):
    response = client.filestorage.drives.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_drives_retrieve(client):
    drives_response = client.filestorage.drives.list(page_size=1)
        
    assert drives_response.results, "No drives available to test retrieve"
    drive_id = drives_response.results[0].id
    drive = client.filestorage.drives.retrieve(id=drive_id)
    assert drive is not None
    assert drive.id == drive_id

def test_folders_list(client):
    response = client.filestorage.folders.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_list(client):
    response = client.filestorage.users.list()    
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_retrieve(client):
    users_response = client.filestorage.users.list(page_size=1)
        
    assert users_response.results, "No users available to test retrieve"
        
    user_id = users_response.results[0].id
    user = client.filestorage.users.retrieve(id=user_id)
        
    assert user is not None
    assert user.id == user_id

def test_groups_list(client):
    response = client.filestorage.groups.list()    
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_audit_trail_list(client):
    response = client.filestorage.audit_trail.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_available_actions_retrieve(client):
    available_actions = client.filestorage.available_actions.retrieve()
        
    assert available_actions is not None

def test_linked_accounts_list(client):
    response = client.filestorage.linked_accounts.list()
        
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_scopes_default_scopes_retrieve(client):
    response = client.filestorage.scopes.default_scopes_retrieve()
        
    assert response is not None

def test_scopes_linked_account_scopes_retrieve(client):
    response = client.filestorage.scopes.linked_account_scopes_retrieve()
        
    assert response is not None
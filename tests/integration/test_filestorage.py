import os
import pytest
from merge import Merge


class TestFilestorageIntegration:
    @pytest.fixture
    def client(self):
        account_token = os.environ["ACCOUNT_TOKEN"]
        api_key = os.environ["API_KEY"]
        
        return Merge(
            account_token=account_token,
            api_key=api_key,
        )

    def test_files_list(self, client):
        response = client.filestorage.files.list()
        
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

    def test_files_retrieve(self, client):
        files_response = client.filestorage.files.list(page_size=1)
        
        assert files_response.results, "No files available to test retrieve"
        
        file_id = files_response.results[0].id
        file = client.filestorage.files.retrieve(id=file_id)
        
        assert file is not None
        assert file.id == file_id

    def test_sync_status_list(self, client):
        response = client.filestorage.sync_status.list()
        
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

    def test_account_details_retrieve(self, client):
        account_details = client.filestorage.account_details.retrieve()
        
        assert account_details is not None
        assert hasattr(account_details, 'id')

    def test_drives_list(self, client):
        response = client.filestorage.drives.list()
        
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

    def test_drives_retrieve(self, client):
        drives_response = client.filestorage.drives.list(page_size=1)
        
        assert drives_response.results, "No drives available to test retrieve"
        
        drive_id = drives_response.results[0].id
        drive = client.filestorage.drives.retrieve(id=drive_id)
        
        assert drive is not None
        assert drive.id == drive_id

    def test_folders_list(self, client):
        response = client.filestorage.folders.list()
        
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

    def test_folders_retrieve(self, client):
        folders_response = client.filestorage.folders.list(page_size=1)
        
        assert folders_response.results, "No folders available to test retrieve"
        
        folder_id = folders_response.results[0].id
        folder = client.filestorage.folders.retrieve(id=folder_id)
        
        assert folder is not None
        assert folder.id == folder_id

    def test_users_list(self, client):
        response = client.filestorage.users.list()
        
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

    def test_users_retrieve(self, client):
        users_response = client.filestorage.users.list(page_size=1)
        
        assert users_response.results, "No users available to test retrieve"
        
        user_id = users_response.results[0].id
        user = client.filestorage.users.retrieve(id=user_id)
        
        assert user is not None
        assert user.id == user_id

    def test_groups_list(self, client):
        response = client.filestorage.groups.list()
        
        assert response is not None
        assert hasattr(response, 'results')
        assert isinstance(response.results, list)

    def test_groups_retrieve(self, client):
        groups_response = client.filestorage.groups.list(page_size=1)
        
        assert groups_response.results, "No groups available to test retrieve"
        
        group_id = groups_response.results[0].id
        group = client.filestorage.groups.retrieve(id=group_id)
        
        assert group is not None
        assert group.id == group_id
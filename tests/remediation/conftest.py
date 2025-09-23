from unittest.mock import MagicMock

import pytest


@pytest.fixture(scope="function")
def mock_client_wrapper() -> MagicMock:
    """Provides a mock SyncClientWrapper for tests."""
    return MagicMock()

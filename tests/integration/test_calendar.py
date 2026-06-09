import os
import pytest
from merge import Merge
from merge.resources.calendar.resources.events.types.events_list_request_expand_item import EventsListRequestExpandItem
from merge.resources.calendar.resources.events.types.events_retrieve_request_expand_item import EventsRetrieveRequestExpandItem
from merge.resources.calendar.resources.groups.types.groups_list_request_expand_item import GroupsListRequestExpandItem
from merge.resources.calendar.resources.groups.types.groups_retrieve_request_expand_item import GroupsRetrieveRequestExpandItem


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_CALENDAR_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
            account_token=account_token,
            api_key=api_key,
    )

def test_calendars_list(client):
    response = client.calendar.calendars.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_calendars_retrieve(client):
    calendars_response = client.calendar.calendars.list(page_size=1)

    if calendars_response.results:
        calendar_id = calendars_response.results[0].id
        calendar = client.calendar.calendars.retrieve(id=calendar_id)
        assert calendar is not None
        assert calendar.id == calendar_id

def test_events_list(client):
    response = client.calendar.events.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_events_retrieve(client):
    events_response = client.calendar.events.list(page_size=1)

    if events_response.results:
        event_id = events_response.results[0].id
        event = client.calendar.events.retrieve(id=event_id)
        assert event is not None
        assert event.id == event_id

def test_events_list_with_expand_calendar(client):
    response = client.calendar.events.list(expand=EventsListRequestExpandItem.CALENDAR)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_events_list_with_expand_invitees(client):
    response = client.calendar.events.list(expand=EventsListRequestExpandItem.INVITEES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_events_list_with_expand_locations(client):
    response = client.calendar.events.list(expand=EventsListRequestExpandItem.LOCATIONS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_events_list_with_expand_series(client):
    response = client.calendar.events.list(expand=EventsListRequestExpandItem.SERIES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_events_retrieve_with_expand_calendar(client):
    events_response = client.calendar.events.list(page_size=1)

    if events_response.results:
        event_id = events_response.results[0].id
        event = client.calendar.events.retrieve(id=event_id, expand=EventsRetrieveRequestExpandItem.CALENDAR)
        assert event is not None
        assert event.id == event_id

def test_groups_list(client):
    response = client.calendar.groups.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_retrieve(client):
    groups_response = client.calendar.groups.list(page_size=1)

    if groups_response.results:
        group_id = groups_response.results[0].id
        group = client.calendar.groups.retrieve(id=group_id)
        assert group is not None
        assert group.id == group_id

def test_groups_list_with_expand_child_groups(client):
    response = client.calendar.groups.list(expand=GroupsListRequestExpandItem.CHILD_GROUPS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_list_with_expand_users(client):
    response = client.calendar.groups.list(expand=GroupsListRequestExpandItem.USERS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_groups_retrieve_with_expand_users(client):
    groups_response = client.calendar.groups.list(page_size=1)

    if groups_response.results:
        group_id = groups_response.results[0].id
        group = client.calendar.groups.retrieve(id=group_id, expand=GroupsRetrieveRequestExpandItem.USERS)
        assert group is not None
        assert group.id == group_id

def test_series_list(client):
    response = client.calendar.series.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_series_retrieve(client):
    series_response = client.calendar.series.list(page_size=1)

    if series_response.results:
        series_id = series_response.results[0].id
        series = client.calendar.series.retrieve(id=series_id)
        assert series is not None
        assert series.id == series_id

def test_series_list_with_expand_calendar(client):
    response = client.calendar.series.list(expand="calendar")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_list(client):
    response = client.calendar.users.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_users_retrieve(client):
    users_response = client.calendar.users.list(page_size=1)

    if users_response.results:
        user_id = users_response.results[0].id
        user = client.calendar.users.retrieve(id=user_id)
        assert user is not None
        assert user.id == user_id

def test_users_list_with_expand_groups(client):
    response = client.calendar.users.list(expand="groups")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_sync_status_list(client):
    response = client.calendar.sync_status.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_account_details_retrieve(client):
    account_details = client.calendar.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')

def test_audit_trail_list(client):
    response = client.calendar.audit_trail.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)

def test_available_actions_retrieve(client):
    available_actions = client.calendar.available_actions.retrieve()

    assert available_actions is not None

def test_scopes_default_scopes_retrieve(client):
    response = client.calendar.scopes.default_scopes_retrieve()

    assert response is not None

def test_scopes_linked_account_scopes_retrieve(client):
    response = client.calendar.scopes.linked_account_scopes_retrieve()

    assert response is not None

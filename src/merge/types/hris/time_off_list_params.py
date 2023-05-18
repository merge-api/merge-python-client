# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimeOffListParams"]


class TimeOffListParams(TypedDict, total=False):
    approver_id: str
    """If provided, will only return time off for this approver."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    employee_id: str
    """If provided, will only return time off for this employee."""

    expand: List[Literal["approver", "employee"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, only objects synced by Merge after this date time will be returned.
    """

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, only objects synced by Merge before this date time will be
    returned.
    """

    page_size: int
    """Number of results to return per page."""

    remote_fields: Literal[
        "request_type",
        "request_type,status",
        "request_type,status,units",
        "request_type,units",
        "status",
        "status,units",
        "units",
    ]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    request_type: Optional[Literal["BEREAVEMENT", "JURY_DUTY", "PERSONAL", "SICK", "VACATION", "VOLUNTEER"]]
    """If provided, will only return TimeOff with this request type.

    Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER',
    'BEREAVEMENT')

    - `VACATION` - VACATION
    - `SICK` - SICK
    - `PERSONAL` - PERSONAL
    - `JURY_DUTY` - JURY_DUTY
    - `VOLUNTEER` - VOLUNTEER
    - `BEREAVEMENT` - BEREAVEMENT
    """

    show_enum_origins: Literal[
        "request_type",
        "request_type,status",
        "request_type,status,units",
        "request_type,units",
        "status",
        "status,units",
        "units",
    ]
    """Which fields should be returned in non-normalized form."""

    status: Optional[Literal["APPROVED", "CANCELLED", "DECLINED", "DELETED", "REQUESTED"]]
    """If provided, will only return TimeOff with this status.

    Options: ('REQUESTED', 'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')

    - `REQUESTED` - REQUESTED
    - `APPROVED` - APPROVED
    - `DECLINED` - DECLINED
    - `CANCELLED` - CANCELLED
    - `DELETED` - DELETED
    """

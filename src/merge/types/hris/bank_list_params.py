# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BankListParams"]


class BankListParams(TypedDict, total=False):
    account_type: Optional[Literal["CHECKING", "SAVINGS"]]
    """If provided, will only return BankInfo's with this account type.

    Options: ('SAVINGS', 'CHECKING')

    - `SAVINGS` - SAVINGS
    - `CHECKING` - CHECKING
    """

    bank_name: Optional[str]
    """If provided, will only return BankInfo's with this bank name."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    employee_id: str
    """If provided, will only return bank accounts for this employee."""

    expand: List[Literal["employee"]]
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
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    order_by: Literal["-remote_created_at", "remote_created_at"]
    """Overrides the default ordering for this endpoint."""

    page_size: int
    """Number of results to return per page."""

    remote_fields: Literal["account_type"]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    show_enum_origins: Literal["account_type"]
    """Which fields should be returned in non-normalized form."""

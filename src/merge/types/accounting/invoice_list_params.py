# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    company_id: str
    """If provided, will only return invoices for this company."""

    contact_id: str
    """If provided, will only return invoices for this contact."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    expand: Literal[
        "company",
        "contact",
        "contact,company",
        "line_items",
        "line_items,company",
        "line_items,contact",
        "line_items,contact,company",
        "payments",
        "payments,company",
        "payments,contact",
        "payments,contact,company",
        "payments,line_items",
        "payments,line_items,company",
        "payments,line_items,contact",
        "payments,line_items,contact,company",
    ]
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

    issue_date_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    issue_date_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    remote_fields: Literal["type"]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    show_enum_origins: Literal["type"]
    """Which fields should be returned in non-normalized form."""

    type: Optional[Literal["ACCOUNTS_PAYABLE", "ACCOUNTS_RECEIVABLE"]]
    """If provided, will only return Invoices with this type

    - `ACCOUNTS_RECEIVABLE` - ACCOUNTS_RECEIVABLE
    - `ACCOUNTS_PAYABLE` - ACCOUNTS_PAYABLE
    """

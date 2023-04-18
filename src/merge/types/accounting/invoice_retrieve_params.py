# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvoiceRetrieveParams"]


class InvoiceRetrieveParams(TypedDict, total=False):
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

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["type"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["type"]
    """Which fields should be returned in non-normalized form."""

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PurchaseOrderRetrieveParams"]


class PurchaseOrderRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "company",
        "delivery_address",
        "delivery_address,company",
        "delivery_address,vendor",
        "delivery_address,vendor,company",
        "line_items",
        "line_items,company",
        "line_items,delivery_address",
        "line_items,delivery_address,company",
        "line_items,delivery_address,vendor",
        "line_items,delivery_address,vendor,company",
        "line_items,vendor",
        "line_items,vendor,company",
        "vendor",
        "vendor,company",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["status"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["status"]
    """Which fields should be returned in non-normalized form."""

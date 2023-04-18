# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TransactionRetrieveParams"]


class TransactionRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "account",
        "contact",
        "contact,account",
        "line_items",
        "line_items,account",
        "line_items,contact",
        "line_items,contact,account",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

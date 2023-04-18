# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NoteRetrieveParams"]


class NoteRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "account",
        "account,opportunity",
        "contact",
        "contact,account",
        "contact,account,opportunity",
        "contact,opportunity",
        "opportunity",
        "owner",
        "owner,account",
        "owner,account,opportunity",
        "owner,contact",
        "owner,contact,account",
        "owner,contact,account,opportunity",
        "owner,contact,opportunity",
        "owner,opportunity",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    include_remote_fields: bool
    """
    Whether to include all remote fields, including fields that Merge did not map to
    common models, in a normalized format.
    """

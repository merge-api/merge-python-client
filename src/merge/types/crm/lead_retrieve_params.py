# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LeadRetrieveParams"]


class LeadRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "converted_account",
        "converted_contact",
        "converted_contact,converted_account",
        "owner",
        "owner,converted_account",
        "owner,converted_contact",
        "owner,converted_contact,converted_account",
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

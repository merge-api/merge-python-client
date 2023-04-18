# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EngagementRetrieveParams"]


class EngagementRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "account",
        "account,engagement_type",
        "contacts",
        "contacts,account",
        "contacts,account,engagement_type",
        "contacts,engagement_type",
        "contacts,owner",
        "contacts,owner,account",
        "contacts,owner,account,engagement_type",
        "contacts,owner,engagement_type",
        "engagement_type",
        "owner",
        "owner,account",
        "owner,account,engagement_type",
        "owner,engagement_type",
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

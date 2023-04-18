# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ApplicationRetrieveParams"]


class ApplicationRetrieveParams(TypedDict, total=False):
    expand: List[Literal["candidate", "credited_to", "current_stage", "job", "reject_reason"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

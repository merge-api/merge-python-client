# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ApplicationRetrieveParams"]


class ApplicationRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "candidate",
        "candidate,credited_to",
        "candidate,credited_to,current_stage",
        "candidate,credited_to,current_stage,reject_reason",
        "candidate,credited_to,reject_reason",
        "candidate,current_stage",
        "candidate,current_stage,reject_reason",
        "candidate,job",
        "candidate,job,credited_to",
        "candidate,job,credited_to,current_stage",
        "candidate,job,credited_to,current_stage,reject_reason",
        "candidate,job,credited_to,reject_reason",
        "candidate,job,current_stage",
        "candidate,job,current_stage,reject_reason",
        "candidate,job,reject_reason",
        "candidate,reject_reason",
        "credited_to",
        "credited_to,current_stage",
        "credited_to,current_stage,reject_reason",
        "credited_to,reject_reason",
        "current_stage",
        "current_stage,reject_reason",
        "job",
        "job,credited_to",
        "job,credited_to,current_stage",
        "job,credited_to,current_stage,reject_reason",
        "job,credited_to,reject_reason",
        "job,current_stage",
        "job,current_stage,reject_reason",
        "job,reject_reason",
        "reject_reason",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

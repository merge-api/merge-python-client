# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ApplicationChangeStageParams"]


class ApplicationChangeStageParams(TypedDict, total=False):
    job_interview_stage: Optional[str]
    """The interview stage to move the application to."""

    remote_user_id: str

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplicationCreateParams", "Model"]


class Model(TypedDict, total=False):
    applied_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the application was submitted."""

    candidate: Optional[str]
    """The candidate applying."""

    credited_to: Optional[str]
    """The user credited for this application."""

    current_stage: Optional[str]
    """The application's current stage."""

    integration_params: Optional[object]

    job: Optional[str]
    """The job being applied for."""

    linked_account_params: Optional[object]

    reject_reason: Optional[str]
    """The application's reason for rejection."""

    rejected_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the application was rejected."""

    remote_template_id: Optional[str]

    source: Optional[str]
    """The application's source."""


class ApplicationCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Application Object

    ### Description

    The Application Object is used to represent a candidate's journey through a
    particular Job's recruiting process. If a Candidate applies for multiple Jobs,
    there will be a separate Application for each Job if the third-party integration
    allows it.

    ### Usage Example

    Fetch from the `LIST Applications` endpoint and filter by `ID` to show all
    applications.
    """

    remote_user_id: Required[str]

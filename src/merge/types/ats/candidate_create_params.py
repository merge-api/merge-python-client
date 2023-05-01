# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CandidateCreateParams", "Model", "ModelPhoneNumber", "ModelEmailAddress", "ModelURL"]


class ModelPhoneNumber(TypedDict, total=False):
    integration_params: Optional[object]

    linked_account_params: Optional[object]

    phone_number: Optional[str]
    """The phone number."""

    phone_number_type: Literal["HOME", "WORK", "MOBILE", "SKYPE", "OTHER"]
    """
    - `HOME` - HOME
    - `WORK` - WORK
    - `MOBILE` - MOBILE
    - `SKYPE` - SKYPE
    - `OTHER` - OTHER
    """

    value: Optional[str]
    """The phone number."""


class ModelEmailAddress(TypedDict, total=False):
    email_address: Optional[str]
    """The email address."""

    email_address_type: Literal["PERSONAL", "WORK", "OTHER"]
    """
    - `PERSONAL` - PERSONAL
    - `WORK` - WORK
    - `OTHER` - OTHER
    """

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    value: Optional[str]
    """The email address."""


class ModelURL(TypedDict, total=False):
    integration_params: Optional[object]

    linked_account_params: Optional[object]

    url_type: Literal["PERSONAL", "COMPANY", "PORTFOLIO", "BLOG", "SOCIAL_MEDIA", "OTHER", "JOB_POSTING"]
    """
    - `PERSONAL` - PERSONAL
    - `COMPANY` - COMPANY
    - `PORTFOLIO` - PORTFOLIO
    - `BLOG` - BLOG
    - `SOCIAL_MEDIA` - SOCIAL_MEDIA
    - `OTHER` - OTHER
    - `JOB_POSTING` - JOB_POSTING
    """

    value: Optional[str]
    """The site's url."""


class Model(TypedDict, total=False):
    applications: List[Optional[str]]
    """Array of `Application` object IDs."""

    attachments: List[Optional[str]]
    """Array of `Attachment` object IDs."""

    can_email: Optional[bool]
    """Whether or not the candidate can be emailed."""

    company: Optional[str]
    """The candidate's current company."""

    email_addresses: List[ModelEmailAddress]

    first_name: Optional[str]
    """The candidate's first name."""

    integration_params: Optional[object]

    is_private: Optional[bool]
    """Whether or not the candidate is private."""

    last_interaction_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the most recent interaction with the candidate occurred."""

    last_name: Optional[str]
    """The candidate's last name."""

    linked_account_params: Optional[object]

    locations: Optional[List[Optional[str]]]
    """The candidate's locations."""

    phone_numbers: List[ModelPhoneNumber]

    remote_template_id: Optional[str]

    tags: List[Optional[str]]
    """Array of `Tag` names as strings."""

    title: Optional[str]
    """The candidate's current title."""

    urls: List[ModelURL]


class CandidateCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Candidate Object

    ### Description

    The `Candidate` object is used to represent profile information about a given
    Candidate. Because it is specific to a Candidate, this information stays
    constant across applications.

    ### Usage Example

    Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all
    candidates.
    """

    remote_user_id: Required[str]

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountToken", "Integration"]


class Integration(TypedDict, total=False):
    name: Required[str]
    """Company name."""

    api_endpoints_to_documentation_urls: object
    """Mapping of API endpoints to documentation urls for support.

    Example: {'GET':
    [['/common-model-scopes', 'https://docs.merge.dev/accounting/common-model-scopes/#common_model_scopes_retrieve'],['/common-model-actions', 'https://docs.merge.dev/accounting/common-model-actions/#common_model_actions_retrieve']],
    'POST': []}
    """

    categories: List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]]
    """Category or categories this integration belongs to.

    Multiple categories should be comma separated, i.e. [ats, hris].
    """

    color: str
    """
    The color of this integration used for buttons and text throughout the app and
    landing pages. <b>Choose a darker, saturated color.</b>
    """

    image: Optional[str]
    """Company logo in rectangular shape.

    <b>Upload an image with a clear background.</b>
    """

    is_in_beta: bool
    """
    If checked, this integration will not appear in the linking flow, and will
    appear elsewhere with a Beta tag.
    """

    square_image: Optional[str]
    """Company logo in square shape. <b>Upload an image with a white background.</b>"""


class AccountToken(TypedDict, total=False):
    account_token: Required[str]

    integration: Required[Integration]

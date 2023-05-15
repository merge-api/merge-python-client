# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountToken", "Integration"]


class Integration(BaseModel):
    name: str
    """Company name."""

    api_endpoints_to_documentation_urls: Optional[object]
    """Mapping of API endpoints to documentation urls for support.

    Example: {'GET':
    [['/common-model-scopes', 'https://docs.merge.dev/accounting/common-model-scopes/#common_model_scopes_retrieve'],['/common-model-actions', 'https://docs.merge.dev/accounting/common-model-actions/#common_model_actions_retrieve']],
    'POST': []}
    """

    categories: Optional[List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]]]
    """Category or categories this integration belongs to.

    Multiple categories should be comma separated, i.e. [ats, hris].
    """

    color: Optional[str]
    """
    The color of this integration used for buttons and text throughout the app and
    landing pages. <b>Choose a darker, saturated color.</b>
    """

    image: Optional[str]
    """Company logo in rectangular shape.

    <b>Upload an image with a clear background.</b>
    """

    is_in_beta: Optional[bool]
    """
    If checked, this integration will not appear in the linking flow, and will
    appear elsewhere with a Beta tag.
    """

    slug: Optional[str]

    square_image: Optional[str]
    """Company logo in square shape. <b>Upload an image with a white background.</b>"""


class AccountToken(BaseModel):
    account_token: str

    integration: Integration

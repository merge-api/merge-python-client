# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.marketing import template

__all__ = ["MktgTemplateResponse"]


class MktgTemplateResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: template.Template
    """# The Template Object

    ### Description

    The `Template` object is used to represent a template for a marketing asset in
    the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/templates` endpoint and view their content
    properties.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

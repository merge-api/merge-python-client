# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.ats import application

__all__ = ["ApplicationResponse"]


class ApplicationResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: application.Application
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

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

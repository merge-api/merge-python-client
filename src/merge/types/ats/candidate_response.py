# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.ats import candidate

__all__ = ["CandidateResponse"]


class CandidateResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: candidate.Candidate
    """# The Candidate Object

    ### Description

    The `Candidate` object is used to represent profile information about a given
    Candidate. Because it is specific to a Candidate, this information stays
    constant across applications.

    ### Usage Example

    Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all
    candidates.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

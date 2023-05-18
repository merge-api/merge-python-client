# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["EEOC"]


class EEOC(BaseModel):
    candidate: Optional[str]
    """The candidate being represented."""

    disability_status: Optional[
        Literal[
            "YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY",
            "NO_I_DONT_HAVE_A_DISABILITY",
            "I_DONT_WISH_TO_ANSWER",
        ]
    ]
    """
    - `YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY` -
      YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY
    - `NO_I_DONT_HAVE_A_DISABILITY` - NO_I_DONT_HAVE_A_DISABILITY
    - `I_DONT_WISH_TO_ANSWER` - I_DONT_WISH_TO_ANSWER
    """

    field_mappings: Optional[object]

    gender: Optional[Literal["MALE", "FEMALE", "NON-BINARY", "OTHER", "DECLINE_TO_SELF_IDENTIFY"]]
    """
    - `MALE` - MALE
    - `FEMALE` - FEMALE
    - `NON-BINARY` - NON-BINARY
    - `OTHER` - OTHER
    - `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY
    """

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    race: Optional[
        Literal[
            "AMERICAN_INDIAN_OR_ALASKAN_NATIVE",
            "ASIAN",
            "BLACK_OR_AFRICAN_AMERICAN",
            "HISPANIC_OR_LATINO",
            "WHITE",
            "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER",
            "TWO_OR_MORE_RACES",
            "DECLINE_TO_SELF_IDENTIFY",
        ]
    ]
    """
    - `AMERICAN_INDIAN_OR_ALASKAN_NATIVE` - AMERICAN_INDIAN_OR_ALASKAN_NATIVE
    - `ASIAN` - ASIAN
    - `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN
    - `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO
    - `WHITE` - WHITE
    - `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` -
      NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER
    - `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES
    - `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY
    """

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    submitted_at: Optional[datetime]
    """When the information was submitted."""

    veteran_status: Optional[
        Literal[
            "I_AM_NOT_A_PROTECTED_VETERAN",
            "I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN",
            "I_DONT_WISH_TO_ANSWER",
        ]
    ]
    """
    - `I_AM_NOT_A_PROTECTED_VETERAN` - I_AM_NOT_A_PROTECTED_VETERAN
    - `I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN` -
      I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN
    - `I_DONT_WISH_TO_ANSWER` - I_DONT_WISH_TO_ANSWER
    """

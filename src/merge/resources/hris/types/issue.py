# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .issue_status import IssueStatus
import pydantic
import datetime as dt
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Issue(UniversalBaseModel):
    id: typing.Optional[str]
    status: typing.Optional[IssueStatus] = pydantic.Field()
    """
    Status of the issue. Options: ('ONGOING', 'RESOLVED')
    
    - `ONGOING` - ONGOING
    - `RESOLVED` - RESOLVED
    """

    error_description: str
    end_user: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    first_incident_time: typing.Optional[dt.datetime]
    last_incident_time: typing.Optional[dt.datetime]
    is_muted: typing.Optional[bool]
    error_details: typing.Optional[typing.List[str]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

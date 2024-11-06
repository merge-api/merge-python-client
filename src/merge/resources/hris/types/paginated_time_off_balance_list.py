# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .employee import Employee
from .employment import Employment
from .team import Team
import typing
from .time_off_balance import TimeOffBalance
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ....core.pydantic_utilities import update_forward_refs


class PaginatedTimeOffBalanceList(UniversalBaseModel):
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.Optional[typing.List[TimeOffBalance]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Employee, PaginatedTimeOffBalanceList=PaginatedTimeOffBalanceList)
update_forward_refs(Employment, PaginatedTimeOffBalanceList=PaginatedTimeOffBalanceList)
update_forward_refs(Team, PaginatedTimeOffBalanceList=PaginatedTimeOffBalanceList)

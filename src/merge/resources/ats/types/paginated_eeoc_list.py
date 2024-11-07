# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .application import Application
from .candidate import Candidate
from .offer import Offer
import typing
from .eeoc import Eeoc
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ....core.pydantic_utilities import update_forward_refs


class PaginatedEeocList(UniversalBaseModel):
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.Optional[typing.List[Eeoc]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Application, PaginatedEeocList=PaginatedEeocList)
update_forward_refs(Candidate, PaginatedEeocList=PaginatedEeocList)
update_forward_refs(Offer, PaginatedEeocList=PaginatedEeocList)

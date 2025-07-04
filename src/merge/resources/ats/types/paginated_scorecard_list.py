# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ....core.unchecked_base_model import UncheckedBaseModel
from .scorecard import Scorecard


class PaginatedScorecardList(UncheckedBaseModel):
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.Optional[typing.List[Scorecard]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .application import Application  # noqa: E402, F401, I001
from .candidate import Candidate  # noqa: E402, F401, I001
from .offer import Offer  # noqa: E402, F401, I001

update_forward_refs(PaginatedScorecardList)

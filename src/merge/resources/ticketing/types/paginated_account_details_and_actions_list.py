# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .account_details_and_actions import AccountDetailsAndActions
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PaginatedAccountDetailsAndActionsList(UniversalBaseModel):
    next: typing.Optional[str]
    previous: typing.Optional[str]
    results: typing.Optional[typing.List[AccountDetailsAndActions]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

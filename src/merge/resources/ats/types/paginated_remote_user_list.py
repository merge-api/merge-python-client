# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .remote_user import RemoteUser
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PaginatedRemoteUserList(UniversalBaseModel):
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.Optional[typing.List[RemoteUser]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

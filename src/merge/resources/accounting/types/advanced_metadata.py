# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AdvancedMetadata(UniversalBaseModel):
    id: str
    display_name: typing.Optional[str]
    description: typing.Optional[str]
    is_required: typing.Optional[bool]
    is_custom: typing.Optional[bool]
    field_choices: typing.Optional[typing.List[typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

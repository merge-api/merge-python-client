# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .linked_account_status import LinkedAccountStatus


class MetaResponse(UniversalBaseModel):
    request_schema: typing.Dict[str, typing.Any]
    remote_field_classes: typing.Optional[typing.Dict[str, typing.Any]]
    status: typing.Optional[LinkedAccountStatus]
    has_conditional_params: bool
    has_required_linked_account_params: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_integration import AccountIntegration
from .model_operation import ModelOperation


class AvailableActions(UniversalBaseModel):
    """
    # The AvailableActions Object

    ### Description

    The `Activity` object is used to see all available model/operation combinations for an integration.

    ### Usage Example

    Fetch all the actions available for the `Zenefits` integration.
    """

    integration: AccountIntegration
    passthrough_available: bool
    available_model_operations: typing.Optional[typing.List[ModelOperation]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

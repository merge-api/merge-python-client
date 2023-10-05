# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .account_integration import AccountIntegration
from .model_operation import ModelOperation


class AvailableActions(pydantic.BaseModel):
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

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

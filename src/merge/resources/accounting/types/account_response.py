# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .account import Account
from .debug_mode_log import DebugModeLog
from .error_validation_problem import ErrorValidationProblem
from .warning_validation_problem import WarningValidationProblem


class AccountResponse(pydantic.BaseModel):
    model: Account
    warnings: typing.List[WarningValidationProblem]
    errors: typing.List[ErrorValidationProblem]
    logs: typing.Optional[typing.List[DebugModeLog]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
from .opportunity import Opportunity
import typing
from .warning_validation_problem import WarningValidationProblem
from .error_validation_problem import ErrorValidationProblem
from .debug_mode_log import DebugModeLog
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OpportunityResponse(UniversalBaseModel):
    model: Opportunity
    warnings: typing.List[WarningValidationProblem]
    errors: typing.List[ErrorValidationProblem]
    logs: typing.Optional[typing.List[DebugModeLog]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

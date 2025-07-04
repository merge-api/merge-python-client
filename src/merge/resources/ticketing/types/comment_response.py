# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ....core.unchecked_base_model import UncheckedBaseModel
from .comment import Comment
from .debug_mode_log import DebugModeLog
from .error_validation_problem import ErrorValidationProblem
from .warning_validation_problem import WarningValidationProblem


class CommentResponse(UncheckedBaseModel):
    model: Comment
    warnings: typing.List[WarningValidationProblem]
    errors: typing.List[ErrorValidationProblem]
    logs: typing.Optional[typing.List[DebugModeLog]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .attachment import Attachment  # noqa: E402, F401, I001
from .collection import Collection  # noqa: E402, F401, I001
from .ticket import Ticket  # noqa: E402, F401, I001

update_forward_refs(CommentResponse)

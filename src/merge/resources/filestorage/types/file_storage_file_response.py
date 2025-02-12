# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .folder import Folder
from .group import Group
from .file import File
import typing
from .warning_validation_problem import WarningValidationProblem
from .error_validation_problem import ErrorValidationProblem
from .debug_mode_log import DebugModeLog
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ....core.pydantic_utilities import update_forward_refs


class FileStorageFileResponse(UniversalBaseModel):
    model: File
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


update_forward_refs(Folder, FileStorageFileResponse=FileStorageFileResponse)
update_forward_refs(Group, FileStorageFileResponse=FileStorageFileResponse)

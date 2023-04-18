# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.file_storage import file

__all__ = ["FileResponse"]


class FileResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: file.File
    """# The File Object

    ### Description

    The `File` object is used to represent a file in the workspace. The Object
    typically exists under a folder or drive, if it exists.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/files` endpoint and view their files.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

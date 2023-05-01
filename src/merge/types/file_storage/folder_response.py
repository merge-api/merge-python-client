# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.file_storage import folder

__all__ = ["FolderResponse"]


class FolderResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: folder.Folder
    """# The Folder Object

    ### Description

    The `Folder` object is used to represent a collection of files and/or folders in
    the workspace. Could be within a drive, if it exsts.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/folders` endpoint and view their
    folders.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ....types import shared
from ...._models import BaseModel
from ....types.crm.custom_object_classes import association_type

__all__ = ["AssociationTypeResponse"]


class AssociationTypeResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: association_type.AssociationType
    """# The AssociationType Object

    ### Description

    The `Association Type` object represents the relationship between two objects.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]

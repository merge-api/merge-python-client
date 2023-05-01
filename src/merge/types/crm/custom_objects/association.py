# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Association"]


class Association(BaseModel):
    association_type: Optional[str]

    source_object: Optional[object]

    target_object: Optional[object]

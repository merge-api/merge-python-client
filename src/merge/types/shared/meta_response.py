# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MetaResponse", "Status"]


class Status(BaseModel):
    can_make_request: bool

    linked_account_status: str


class MetaResponse(BaseModel):
    has_conditional_params: bool

    has_required_linked_account_params: bool

    request_schema: object

    remote_field_classes: Optional[object]

    status: Optional[Status]

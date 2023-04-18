# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MetaResponse", "Status"]


class Status(TypedDict, total=False):
    can_make_request: Required[bool]

    linked_account_status: Required[str]


class MetaResponse(TypedDict, total=False):
    has_conditional_params: Required[bool]

    has_required_linked_account_params: Required[bool]

    request_schema: Required[object]

    remote_field_classes: object

    status: Status

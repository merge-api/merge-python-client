# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MetaForCreateParams"]


class MetaForCreateParams(TypedDict, total=False):
    application_remote_template_id: str
    """The template ID associated with the nested application in the request."""

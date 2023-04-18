# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateCreateParams", "Model"]


class Model(TypedDict, total=False):
    contents: Optional[str]
    """The template contents."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The template's name."""

    owner: Optional[str]
    """The template's owner."""

    type: Literal["EMAIL", "MESSAGE"]
    """
    - `EMAIL` - EMAIL
    - `MESSAGE` - MESSAGE
    """


class TemplateCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Template Object

    ### Description

    The `Template` object is used to represent a template for a marketing asset in
    the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/templates` endpoint and view their content
    properties.
    """

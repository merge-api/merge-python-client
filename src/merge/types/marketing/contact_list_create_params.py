# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContactListCreateParams", "Model"]


class Model(TypedDict, total=False):
    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The list's name."""

    type: Optional[str]
    """The list's type."""


class ContactListCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The List Object

    ### Description

    The `List` object is used to represent a list of contacts in the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/lists` endpoint and view their names.
    """

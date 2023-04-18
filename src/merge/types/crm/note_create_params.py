# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["NoteCreateParams", "Model"]


class Model(TypedDict, total=False):
    account: Optional[str]
    """The note's account."""

    contact: Optional[str]
    """The note's contact."""

    content: Optional[str]
    """The note's content."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    opportunity: Optional[str]
    """The note's opportunity."""

    owner: Optional[str]
    """The note's owner."""


class NoteCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Note Object

    ### Description

    The `Note` object is used to represent a note on another object.

    ### Usage Example

    TODO
    """

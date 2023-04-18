# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CommentCreateParams", "Model"]


class Model(TypedDict, total=False):
    body: Optional[str]
    """The comment's text body."""

    contact: Optional[str]
    """The author of the Comment, if the author is a Contact."""

    html_body: Optional[str]
    """The comment's text body formatted as html."""

    integration_params: Optional[object]

    is_private: Optional[bool]
    """Whether or not the comment is internal."""

    linked_account_params: Optional[object]

    ticket: Optional[str]
    """The ticket associated with the comment."""

    user: Optional[str]
    """The author of the Comment, if the author is a User."""


class CommentCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Comment Object

    ### Description

    The `Comment` object is used to represent a comment on a ticket.

    ### Usage Example

    TODO
    """

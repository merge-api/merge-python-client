# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkTokenCreateParams", "CommonModel"]


class CommonModel(TypedDict, total=False):
    disabled_fields: Required[List[str]]

    enabled_actions: Required[List[Literal["READ", "WRITE"]]]

    model_id: Required[str]


class LinkTokenCreateParams(TypedDict, total=False):
    categories: Required[List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]]]
    """The integration categories to show in Merge Link."""

    end_user_email_address: Required[str]
    """Your end user's email address.

    This is purely for identification purposes - setting this value will not cause
    any emails to be sent.
    """

    end_user_organization_name: Required[str]
    """Your end user's organization."""

    end_user_origin_id: Required[str]
    """
    This unique identifier typically represents the ID for your end user in your
    product's database. This value must be distinct from other Linked Accounts'
    unique identifiers.
    """

    common_models: Optional[List[CommonModel]]
    """
    An array of objects to specify the models and fields that will be disabled for a
    given Linked Account. Each object uses model_id, enabled_actions, and
    disabled_fields to specify the model, method, and fields that are scoped for a
    given Linked Account.
    """

    integration: Optional[str]
    """The slug of a specific pre-selected integration for this linking flow token.

    For examples of slugs, see
    https://www.merge.dev/docs/basics/integration-metadata/.
    """

    link_expiry_mins: int
    """
    An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL]
    for how long this token is valid. Defaults to 30.
    """

    should_create_magic_link_url: Optional[bool]
    """Whether to generate a Magic Link URL.

    Defaults to false. For more information on Magic Link, see
    https://merge.dev/blog/product/integrations,-fast.-say-hello-to-magic-link/.
    """

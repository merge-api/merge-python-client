# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .category_enum import CategoryEnum


class AccountDetails(UniversalBaseModel):
    id: typing.Optional[str]
    integration: typing.Optional[str]
    integration_slug: typing.Optional[str]
    category: typing.Optional[CategoryEnum]
    end_user_origin_id: typing.Optional[str]
    end_user_organization_name: typing.Optional[str]
    end_user_email_address: typing.Optional[str]
    status: typing.Optional[str]
    webhook_listener_url: typing.Optional[str]
    is_duplicate: typing.Optional[bool] = pydantic.Field()
    """
    Whether a Production Linked Account's credentials match another existing Production Linked Account. This field is `null` for Test Linked Accounts, incomplete Production Linked Accounts, and ignored duplicate Production Linked Account sets.
    """

    account_type: typing.Optional[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

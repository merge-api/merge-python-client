# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .categories_enum import CategoriesEnum


class AccountIntegration(UncheckedBaseModel):
    name: str = pydantic.Field()
    """
    Company name.
    """

    abbreviated_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional. This shortened name appears in places with limited space, usually in conjunction with the platform's logo (e.g., Merge Link menu).<br><br>Example: <i>Workforce Now (in lieu of ADP Workforce Now), SuccessFactors (in lieu of SAP SuccessFactors)</i>
    """

    categories: typing.Optional[typing.List[CategoriesEnum]] = pydantic.Field(default=None)
    """
    Category or categories this integration belongs to. Multiple categories should be comma separated, i.e. [ats, hris].
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company logo in rectangular shape.
    """

    square_image: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company logo in square shape.
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The color of this integration used for buttons and text throughout the app and landing pages. <b>Choose a darker, saturated color.</b>
    """

    slug: typing.Optional[str] = None
    api_endpoints_to_documentation_urls: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = (
        pydantic.Field(default=None)
    )
    """
    Mapping of API endpoints to documentation urls for support. Example: {'GET': [['/common-model-scopes', 'https://docs.merge.dev/accounting/common-model-scopes/#common_model_scopes_retrieve'],['/common-model-actions', 'https://docs.merge.dev/accounting/common-model-actions/#common_model_actions_retrieve']], 'POST': []}
    """

    webhook_setup_guide_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Setup guide URL for third party webhook creation. Exposed in Merge Docs.
    """

    category_beta_status: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Category or categories this integration is in beta status for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

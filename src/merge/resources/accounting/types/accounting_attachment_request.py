# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AccountingAttachmentRequest(UniversalBaseModel):
    """
    # The Accounting Attachment Object

    ### Description

    The `AccountingAttachment` object is used to represent a company's attachments.

    ### Usage Example

    Fetch from the `LIST AccountingAttachments` endpoint and view a company's attachments.
    """

    file_name: typing.Optional[str] = pydantic.Field()
    """
    The attachment's name.
    """

    file_url: typing.Optional[str] = pydantic.Field()
    """
    The attachment's url.
    """

    company: typing.Optional[str] = pydantic.Field()
    """
    The company the accounting attachment belongs to.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .attachment_request_attachment_type import AttachmentRequestAttachmentType
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class AttachmentRequest(UniversalBaseModel):
    """
    # The Attachment Object

    ### Description

    The `Attachment` object is used to represent a file attached to a candidate.

    ### Usage Example

    Fetch from the `LIST Attachments` endpoint and view attachments accessible by a company.
    """

    file_name: typing.Optional[str] = pydantic.Field()
    """
    The attachment's name.
    """

    file_url: typing.Optional[str] = pydantic.Field()
    """
    The attachment's url.
    """

    candidate: typing.Optional[str] = pydantic.Field()
    """
    
    """

    attachment_type: typing.Optional[AttachmentRequestAttachmentType] = pydantic.Field()
    """
    The attachment's type.
    
    - `RESUME` - RESUME
    - `COVER_LETTER` - COVER_LETTER
    - `OFFER_LETTER` - OFFER_LETTER
    - `OTHER` - OTHER
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
from .method_enum import MethodEnum
import pydantic
import typing
from .multipart_form_field_request import MultipartFormFieldRequest
from .request_format_enum import RequestFormatEnum
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class DataPassthroughRequest(UniversalBaseModel):
    """
    # The DataPassthrough Object

    ### Description

    The `DataPassthrough` object is used to send information to an otherwise-unsupported third-party endpoint.

    ### Usage Example

    Create a `DataPassthrough` to get team hierarchies from your Rippling integration.
    """

    method: MethodEnum
    path: str = pydantic.Field()
    """
    The path of the request in the third party's platform.
    """

    base_url_override: typing.Optional[str] = pydantic.Field()
    """
    An optional override of the third party's base url for the request.
    """

    data: typing.Optional[str] = pydantic.Field()
    """
    The data with the request. You must include a `request_format` parameter matching the data's format
    """

    multipart_form_data: typing.Optional[typing.List[MultipartFormFieldRequest]] = pydantic.Field()
    """
    Pass an array of `MultipartFormField` objects in here instead of using the `data` param if `request_format` is set to `MULTIPART`.
    """

    headers: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field()
    """
    The headers to use for the request (Merge will handle the account's authorization headers). `Content-Type` header is required for passthrough. Choose content type corresponding to expected format of receiving server.
    """

    request_format: typing.Optional[RequestFormatEnum]
    normalize_response: typing.Optional[bool] = pydantic.Field()
    """
    Optional. If true, the response will always be an object of the form `{"type": T, "value": ...}` where `T` will be one of `string, boolean, number, null, array, object`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

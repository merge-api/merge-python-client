# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PassthroughRequestSendParams", "Multipartformdata"]


class Multipartformdata(TypedDict, total=False):
    data: Required[str]
    """The data for the form field."""

    name: Required[str]
    """The name of the form field"""

    content_type: Optional[str]
    """The MIME type of the file, if the field is for a file."""

    encoding: Literal["RAW", "BASE64", "GZIP_BASE64"]
    """
    - `RAW` - RAW
    - `BASE64` - BASE64
    - `GZIP_BASE64` - GZIP_BASE64
    """

    file_name: Optional[str]
    """The file name of the form field, if the field is for a file."""


class PassthroughRequestSendParams(TypedDict, total=False):
    method: Required[Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]]
    """
    - `GET` - GET
    - `OPTIONS` - OPTIONS
    - `HEAD` - HEAD
    - `POST` - POST
    - `PUT` - PUT
    - `PATCH` - PATCH
    - `DELETE` - DELETE
    """

    path: Required[str]

    base_url_override: Optional[str]

    data: Optional[str]

    headers: Optional[object]
    """
    The headers to use for the request (Merge will handle the account's
    authorization headers). `Content-Type` header is required for passthrough.
    Choose content type corresponding to expected format of receiving server.
    """

    multipart_form_data: Optional[List[Multipartformdata]]
    """
    Pass an array of `MultipartFormField` objects in here instead of using the
    `data` param if `request_format` is set to `MULTIPART`.
    """

    normalize_response: bool
    """Optional.

    If true, the response will always be an object of the form
    `{"type": T, "value": ...}` where `T` will be one of
    `string, boolean, number, null, array, object`.
    """

    request_format: Literal["JSON", "XML", "MULTIPART"]
    """
    - `JSON` - JSON
    - `XML` - XML
    - `MULTIPART` - MULTIPART
    """

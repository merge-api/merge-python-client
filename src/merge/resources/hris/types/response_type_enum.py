# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResponseTypeEnum(str, enum.Enum):
    """
    - `JSON` - JSON
    - `BASE64_GZIP` - BASE64_GZIP
    """

    JSON = "JSON"
    BASE_64_GZIP = "BASE64_GZIP"

    def visit(self, json: typing.Callable[[], T_Result], base_64_gzip: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseTypeEnum.JSON:
            return json()
        if self is ResponseTypeEnum.BASE_64_GZIP:
            return base_64_gzip()

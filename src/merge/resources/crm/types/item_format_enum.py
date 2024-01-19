# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ItemFormatEnum(str, enum.Enum):
    """
    - `string` - uuid
    - `number` - url
    - `date` - email
    - `datetime` - phone
    - `bool` - currency
    - `list` - decimal
    """

    STRING = "string"
    NUMBER = "number"
    DATE = "date"
    DATETIME = "datetime"
    BOOL = "bool"
    LIST = "list"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        bool: typing.Callable[[], T_Result],
        list: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemFormatEnum.STRING:
            return string()
        if self is ItemFormatEnum.NUMBER:
            return number()
        if self is ItemFormatEnum.DATE:
            return date()
        if self is ItemFormatEnum.DATETIME:
            return datetime()
        if self is ItemFormatEnum.BOOL:
            return bool()
        if self is ItemFormatEnum.LIST:
            return list()

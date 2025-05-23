# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ComponentTypeEnum(str, enum.Enum):
    """
    * `SALES` - SALES
    * `PURCHASE` - PURCHASE
    """

    SALES = "SALES"
    PURCHASE = "PURCHASE"

    def visit(self, sales: typing.Callable[[], T_Result], purchase: typing.Callable[[], T_Result]) -> T_Result:
        if self is ComponentTypeEnum.SALES:
            return sales()
        if self is ComponentTypeEnum.PURCHASE:
            return purchase()

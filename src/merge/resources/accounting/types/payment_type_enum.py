# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PaymentTypeEnum(str, enum.Enum):
    """
    - `ACCOUNTS_PAYABLE` - ACCOUNTS_PAYABLE
    - `ACCOUNTS_RECEIVABLE` - ACCOUNTS_RECEIVABLE
    """

    ACCOUNTS_PAYABLE = "ACCOUNTS_PAYABLE"
    ACCOUNTS_RECEIVABLE = "ACCOUNTS_RECEIVABLE"

    def visit(
        self, accounts_payable: typing.Callable[[], T_Result], accounts_receivable: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PaymentTypeEnum.ACCOUNTS_PAYABLE:
            return accounts_payable()
        if self is PaymentTypeEnum.ACCOUNTS_RECEIVABLE:
            return accounts_receivable()

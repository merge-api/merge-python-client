# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceTypeEnum(str, enum.Enum):
    """
    - `ACCOUNTS_RECEIVABLE` - ACCOUNTS_RECEIVABLE
    - `ACCOUNTS_PAYABLE` - ACCOUNTS_PAYABLE
    """

    ACCOUNTS_RECEIVABLE = "ACCOUNTS_RECEIVABLE"
    ACCOUNTS_PAYABLE = "ACCOUNTS_PAYABLE"

    def visit(
        self, accounts_receivable: typing.Callable[[], T_Result], accounts_payable: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is InvoiceTypeEnum.ACCOUNTS_RECEIVABLE:
            return accounts_receivable()
        if self is InvoiceTypeEnum.ACCOUNTS_PAYABLE:
            return accounts_payable()

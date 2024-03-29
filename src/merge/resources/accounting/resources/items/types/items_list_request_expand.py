# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ItemsListRequestExpand(str, enum.Enum):
    COMPANY = "company"
    PURCHASE_ACCOUNT = "purchase_account"
    PURCHASE_ACCOUNT_COMPANY = "purchase_account,company"
    PURCHASE_ACCOUNT_SALES_ACCOUNT = "purchase_account,sales_account"
    PURCHASE_ACCOUNT_SALES_ACCOUNT_COMPANY = "purchase_account,sales_account,company"
    SALES_ACCOUNT = "sales_account"
    SALES_ACCOUNT_COMPANY = "sales_account,company"

    def visit(
        self,
        company: typing.Callable[[], T_Result],
        purchase_account: typing.Callable[[], T_Result],
        purchase_account_company: typing.Callable[[], T_Result],
        purchase_account_sales_account: typing.Callable[[], T_Result],
        purchase_account_sales_account_company: typing.Callable[[], T_Result],
        sales_account: typing.Callable[[], T_Result],
        sales_account_company: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemsListRequestExpand.COMPANY:
            return company()
        if self is ItemsListRequestExpand.PURCHASE_ACCOUNT:
            return purchase_account()
        if self is ItemsListRequestExpand.PURCHASE_ACCOUNT_COMPANY:
            return purchase_account_company()
        if self is ItemsListRequestExpand.PURCHASE_ACCOUNT_SALES_ACCOUNT:
            return purchase_account_sales_account()
        if self is ItemsListRequestExpand.PURCHASE_ACCOUNT_SALES_ACCOUNT_COMPANY:
            return purchase_account_sales_account_company()
        if self is ItemsListRequestExpand.SALES_ACCOUNT:
            return sales_account()
        if self is ItemsListRequestExpand.SALES_ACCOUNT_COMPANY:
            return sales_account_company()

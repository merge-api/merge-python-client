# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GeneralLedgerTransactionsRetrieveRequestExpand(str, enum.Enum):
    ACCOUNTING_PERIOD = "accounting_period"
    COMPANY = "company"
    COMPANY_ACCOUNTING_PERIOD = "company,accounting_period"
    GENERAL_LEDGER_TRANSACTION_LINES = "general_ledger_transaction_lines"
    GENERAL_LEDGER_TRANSACTION_LINES_ACCOUNTING_PERIOD = "general_ledger_transaction_lines,accounting_period"
    GENERAL_LEDGER_TRANSACTION_LINES_COMPANY = "general_ledger_transaction_lines,company"
    GENERAL_LEDGER_TRANSACTION_LINES_COMPANY_ACCOUNTING_PERIOD = (
        "general_ledger_transaction_lines,company,accounting_period"
    )
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "tracking_categories,accounting_period"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,company,accounting_period"
    TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES = "tracking_categories,general_ledger_transaction_lines"
    TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES_ACCOUNTING_PERIOD = (
        "tracking_categories,general_ledger_transaction_lines,accounting_period"
    )
    TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES_COMPANY = (
        "tracking_categories,general_ledger_transaction_lines,company"
    )
    TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES_COMPANY_ACCOUNTING_PERIOD = (
        "tracking_categories,general_ledger_transaction_lines,company,accounting_period"
    )

    def visit(
        self,
        accounting_period: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        company_accounting_period: typing.Callable[[], T_Result],
        general_ledger_transaction_lines: typing.Callable[[], T_Result],
        general_ledger_transaction_lines_accounting_period: typing.Callable[[], T_Result],
        general_ledger_transaction_lines_company: typing.Callable[[], T_Result],
        general_ledger_transaction_lines_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_general_ledger_transaction_lines: typing.Callable[[], T_Result],
        tracking_categories_general_ledger_transaction_lines_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_general_ledger_transaction_lines_company: typing.Callable[[], T_Result],
        tracking_categories_general_ledger_transaction_lines_company_accounting_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.ACCOUNTING_PERIOD:
            return accounting_period()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.COMPANY:
            return company()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.COMPANY_ACCOUNTING_PERIOD:
            return company_accounting_period()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.GENERAL_LEDGER_TRANSACTION_LINES:
            return general_ledger_transaction_lines()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.GENERAL_LEDGER_TRANSACTION_LINES_ACCOUNTING_PERIOD:
            return general_ledger_transaction_lines_accounting_period()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.GENERAL_LEDGER_TRANSACTION_LINES_COMPANY:
            return general_ledger_transaction_lines_company()
        if (
            self
            is GeneralLedgerTransactionsRetrieveRequestExpand.GENERAL_LEDGER_TRANSACTION_LINES_COMPANY_ACCOUNTING_PERIOD
        ):
            return general_ledger_transaction_lines_company_accounting_period()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return tracking_categories_accounting_period()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_company_accounting_period()
        if self is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES:
            return tracking_categories_general_ledger_transaction_lines()
        if (
            self
            is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES_ACCOUNTING_PERIOD
        ):
            return tracking_categories_general_ledger_transaction_lines_accounting_period()
        if (
            self
            is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES_COMPANY
        ):
            return tracking_categories_general_ledger_transaction_lines_company()
        if (
            self
            is GeneralLedgerTransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_GENERAL_LEDGER_TRANSACTION_LINES_COMPANY_ACCOUNTING_PERIOD
        ):
            return tracking_categories_general_ledger_transaction_lines_company_accounting_period()

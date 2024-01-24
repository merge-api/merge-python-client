# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LinkedAccountsListRequestCategory(str, enum.Enum):
    ACCOUNTING = "accounting"
    ATS = "ats"
    CRM = "crm"
    FILESTORAGE = "filestorage"
    HRIS = "hris"
    MKTG = "mktg"
    TICKETING = "ticketing"

    def visit(
        self,
        accounting: typing.Callable[[], T_Result],
        ats: typing.Callable[[], T_Result],
        crm: typing.Callable[[], T_Result],
        filestorage: typing.Callable[[], T_Result],
        hris: typing.Callable[[], T_Result],
        mktg: typing.Callable[[], T_Result],
        ticketing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkedAccountsListRequestCategory.ACCOUNTING:
            return accounting()
        if self is LinkedAccountsListRequestCategory.ATS:
            return ats()
        if self is LinkedAccountsListRequestCategory.CRM:
            return crm()
        if self is LinkedAccountsListRequestCategory.FILESTORAGE:
            return filestorage()
        if self is LinkedAccountsListRequestCategory.HRIS:
            return hris()
        if self is LinkedAccountsListRequestCategory.MKTG:
            return mktg()
        if self is LinkedAccountsListRequestCategory.TICKETING:
            return ticketing()
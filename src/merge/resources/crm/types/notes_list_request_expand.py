# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NotesListRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNT_OPPORTUNITY = "account,opportunity"
    CONTACT = "contact"
    CONTACT_ACCOUNT = "contact,account"
    CONTACT_ACCOUNT_OPPORTUNITY = "contact,account,opportunity"
    CONTACT_OPPORTUNITY = "contact,opportunity"
    OPPORTUNITY = "opportunity"
    OWNER = "owner"
    OWNER_ACCOUNT = "owner,account"
    OWNER_ACCOUNT_OPPORTUNITY = "owner,account,opportunity"
    OWNER_CONTACT = "owner,contact"
    OWNER_CONTACT_ACCOUNT = "owner,contact,account"
    OWNER_CONTACT_ACCOUNT_OPPORTUNITY = "owner,contact,account,opportunity"
    OWNER_CONTACT_OPPORTUNITY = "owner,contact,opportunity"
    OWNER_OPPORTUNITY = "owner,opportunity"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        account_opportunity: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_account: typing.Callable[[], T_Result],
        contact_account_opportunity: typing.Callable[[], T_Result],
        contact_opportunity: typing.Callable[[], T_Result],
        opportunity: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
        owner_account: typing.Callable[[], T_Result],
        owner_account_opportunity: typing.Callable[[], T_Result],
        owner_contact: typing.Callable[[], T_Result],
        owner_contact_account: typing.Callable[[], T_Result],
        owner_contact_account_opportunity: typing.Callable[[], T_Result],
        owner_contact_opportunity: typing.Callable[[], T_Result],
        owner_opportunity: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotesListRequestExpand.ACCOUNT:
            return account()
        if self is NotesListRequestExpand.ACCOUNT_OPPORTUNITY:
            return account_opportunity()
        if self is NotesListRequestExpand.CONTACT:
            return contact()
        if self is NotesListRequestExpand.CONTACT_ACCOUNT:
            return contact_account()
        if self is NotesListRequestExpand.CONTACT_ACCOUNT_OPPORTUNITY:
            return contact_account_opportunity()
        if self is NotesListRequestExpand.CONTACT_OPPORTUNITY:
            return contact_opportunity()
        if self is NotesListRequestExpand.OPPORTUNITY:
            return opportunity()
        if self is NotesListRequestExpand.OWNER:
            return owner()
        if self is NotesListRequestExpand.OWNER_ACCOUNT:
            return owner_account()
        if self is NotesListRequestExpand.OWNER_ACCOUNT_OPPORTUNITY:
            return owner_account_opportunity()
        if self is NotesListRequestExpand.OWNER_CONTACT:
            return owner_contact()
        if self is NotesListRequestExpand.OWNER_CONTACT_ACCOUNT:
            return owner_contact_account()
        if self is NotesListRequestExpand.OWNER_CONTACT_ACCOUNT_OPPORTUNITY:
            return owner_contact_account_opportunity()
        if self is NotesListRequestExpand.OWNER_CONTACT_OPPORTUNITY:
            return owner_contact_opportunity()
        if self is NotesListRequestExpand.OWNER_OPPORTUNITY:
            return owner_opportunity()
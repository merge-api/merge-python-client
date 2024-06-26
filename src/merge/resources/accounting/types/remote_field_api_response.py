# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .remote_field_api import RemoteFieldApi


class RemoteFieldApiResponse(pydantic_v1.BaseModel):
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Account")
    accounting_attachment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(
        alias="AccountingAttachment"
    )
    balance_sheet: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="BalanceSheet")
    cash_flow_statement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="CashFlowStatement")
    company_info: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="CompanyInfo")
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Contact")
    income_statement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="IncomeStatement")
    credit_note: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="CreditNote")
    item: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Item")
    purchase_order: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="PurchaseOrder")
    tracking_category: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="TrackingCategory")
    journal_entry: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="JournalEntry")
    tax_rate: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="TaxRate")
    invoice: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Invoice")
    payment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Payment")
    expense: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Expense")
    vendor_credit: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="VendorCredit")
    transaction: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Transaction")
    general_ledger_transaction: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(
        alias="GeneralLedgerTransaction"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

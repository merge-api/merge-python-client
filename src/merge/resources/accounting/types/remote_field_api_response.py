# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .remote_field_api import RemoteFieldApi
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RemoteFieldApiResponse(UniversalBaseModel):
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Account")
    accounting_attachment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="AccountingAttachment")
    balance_sheet: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="BalanceSheet")
    cash_flow_statement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="CashFlowStatement")
    company_info: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="CompanyInfo")
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Contact")
    income_statement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="IncomeStatement")
    credit_note: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="CreditNote")
    item: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Item")
    purchase_order: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="PurchaseOrder")
    tracking_category: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="TrackingCategory")
    journal_entry: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="JournalEntry")
    tax_rate: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="TaxRate")
    invoice: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Invoice")
    payment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Payment")
    expense: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Expense")
    vendor_credit: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="VendorCredit")
    transaction: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Transaction")
    accounting_period: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="AccountingPeriod")
    general_ledger_transaction: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(
        alias="GeneralLedgerTransaction"
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

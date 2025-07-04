# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .field_mapping_api_instance import FieldMappingApiInstance


class FieldMappingApiInstanceResponse(UncheckedBaseModel):
    account: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Account", default=None)
    accounting_attachment: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="AccountingAttachment", default=None
    )
    balance_sheet: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="BalanceSheet", default=None
    )
    cash_flow_statement: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="CashFlowStatement", default=None
    )
    company_info: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="CompanyInfo", default=None
    )
    contact: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Contact", default=None)
    income_statement: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="IncomeStatement", default=None
    )
    credit_note: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="CreditNote", default=None
    )
    item: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Item", default=None)
    purchase_order: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="PurchaseOrder", default=None
    )
    tracking_category: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="TrackingCategory", default=None
    )
    journal_entry: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="JournalEntry", default=None
    )
    tax_rate: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="TaxRate", default=None)
    invoice: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Invoice", default=None)
    payment: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Payment", default=None)
    expense: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Expense", default=None)
    vendor_credit: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="VendorCredit", default=None
    )
    transaction: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="Transaction", default=None
    )
    accounting_period: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="AccountingPeriod", default=None
    )
    general_ledger_transaction: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="GeneralLedgerTransaction", default=None
    )
    bank_feed_account: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="BankFeedAccount", default=None
    )
    employee: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Employee", default=None)
    payment_method: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="PaymentMethod", default=None
    )
    project: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Project", default=None)
    payment_term: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="PaymentTerm", default=None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

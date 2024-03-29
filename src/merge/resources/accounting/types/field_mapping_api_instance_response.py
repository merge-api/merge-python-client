# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .field_mapping_api_instance import FieldMappingApiInstance

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FieldMappingApiInstanceResponse(pydantic.BaseModel):
    account: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Account")
    accounting_attachment: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="AccountingAttachment"
    )
    balance_sheet: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="BalanceSheet")
    cash_flow_statement: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="CashFlowStatement"
    )
    company_info: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="CompanyInfo")
    contact: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Contact")
    income_statement: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="IncomeStatement")
    credit_note: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="CreditNote")
    item: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Item")
    purchase_order: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="PurchaseOrder")
    tracking_category: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="TrackingCategory")
    journal_entry: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="JournalEntry")
    tax_rate: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="TaxRate")
    invoice: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Invoice")
    payment: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Payment")
    expense: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Expense")
    vendor_credit: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="VendorCredit")
    transaction: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Transaction")
    general_ledger_transaction: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="GeneralLedgerTransaction"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}

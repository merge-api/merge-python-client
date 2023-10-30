# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PurchaseOrdersListRequestExpand(str, enum.Enum):
    ACCOUNTING_PERIOD = "accounting_period"
    COMPANY = "company"
    COMPANY_ACCOUNTING_PERIOD = "company,accounting_period"
    DELIVERY_ADDRESS = "delivery_address"
    DELIVERY_ADDRESS_ACCOUNTING_PERIOD = "delivery_address,accounting_period"
    DELIVERY_ADDRESS_COMPANY = "delivery_address,company"
    DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD = "delivery_address,company,accounting_period"
    DELIVERY_ADDRESS_VENDOR = "delivery_address,vendor"
    DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD = "delivery_address,vendor,accounting_period"
    DELIVERY_ADDRESS_VENDOR_COMPANY = "delivery_address,vendor,company"
    DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD = "delivery_address,vendor,company,accounting_period"
    LINE_ITEMS = "line_items"
    LINE_ITEMS_ACCOUNTING_PERIOD = "line_items,accounting_period"
    LINE_ITEMS_COMPANY = "line_items,company"
    LINE_ITEMS_COMPANY_ACCOUNTING_PERIOD = "line_items,company,accounting_period"
    LINE_ITEMS_DELIVERY_ADDRESS = "line_items,delivery_address"
    LINE_ITEMS_DELIVERY_ADDRESS_ACCOUNTING_PERIOD = "line_items,delivery_address,accounting_period"
    LINE_ITEMS_DELIVERY_ADDRESS_COMPANY = "line_items,delivery_address,company"
    LINE_ITEMS_DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD = "line_items,delivery_address,company,accounting_period"
    LINE_ITEMS_DELIVERY_ADDRESS_VENDOR = "line_items,delivery_address,vendor"
    LINE_ITEMS_DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD = "line_items,delivery_address,vendor,accounting_period"
    LINE_ITEMS_DELIVERY_ADDRESS_VENDOR_COMPANY = "line_items,delivery_address,vendor,company"
    LINE_ITEMS_DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,delivery_address,vendor,company,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES = "line_items,tracking_categories"
    LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "line_items,tracking_categories,accounting_period"
    LINE_ITEMS_TRACKING_CATEGORIES_COMPANY = "line_items,tracking_categories,company"
    LINE_ITEMS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,company,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS = "line_items,tracking_categories,delivery_address"
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,delivery_address,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY = "line_items,tracking_categories,delivery_address,company"
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,delivery_address,company,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR = "line_items,tracking_categories,delivery_address,vendor"
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,delivery_address,vendor,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY = (
        "line_items,tracking_categories,delivery_address,vendor,company"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,delivery_address,vendor,company,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_VENDOR = "line_items,tracking_categories,vendor"
    LINE_ITEMS_TRACKING_CATEGORIES_VENDOR_ACCOUNTING_PERIOD = "line_items,tracking_categories,vendor,accounting_period"
    LINE_ITEMS_TRACKING_CATEGORIES_VENDOR_COMPANY = "line_items,tracking_categories,vendor,company"
    LINE_ITEMS_TRACKING_CATEGORIES_VENDOR_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,vendor,company,accounting_period"
    )
    LINE_ITEMS_VENDOR = "line_items,vendor"
    LINE_ITEMS_VENDOR_ACCOUNTING_PERIOD = "line_items,vendor,accounting_period"
    LINE_ITEMS_VENDOR_COMPANY = "line_items,vendor,company"
    LINE_ITEMS_VENDOR_COMPANY_ACCOUNTING_PERIOD = "line_items,vendor,company,accounting_period"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "tracking_categories,accounting_period"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,company,accounting_period"
    TRACKING_CATEGORIES_DELIVERY_ADDRESS = "tracking_categories,delivery_address"
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_ACCOUNTING_PERIOD = "tracking_categories,delivery_address,accounting_period"
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY = "tracking_categories,delivery_address,company"
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD = (
        "tracking_categories,delivery_address,company,accounting_period"
    )
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR = "tracking_categories,delivery_address,vendor"
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD = (
        "tracking_categories,delivery_address,vendor,accounting_period"
    )
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY = "tracking_categories,delivery_address,vendor,company"
    TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD = (
        "tracking_categories,delivery_address,vendor,company,accounting_period"
    )
    TRACKING_CATEGORIES_VENDOR = "tracking_categories,vendor"
    TRACKING_CATEGORIES_VENDOR_ACCOUNTING_PERIOD = "tracking_categories,vendor,accounting_period"
    TRACKING_CATEGORIES_VENDOR_COMPANY = "tracking_categories,vendor,company"
    TRACKING_CATEGORIES_VENDOR_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,vendor,company,accounting_period"
    VENDOR = "vendor"
    VENDOR_ACCOUNTING_PERIOD = "vendor,accounting_period"
    VENDOR_COMPANY = "vendor,company"
    VENDOR_COMPANY_ACCOUNTING_PERIOD = "vendor,company,accounting_period"

    def visit(
        self,
        accounting_period: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        company_accounting_period: typing.Callable[[], T_Result],
        delivery_address: typing.Callable[[], T_Result],
        delivery_address_accounting_period: typing.Callable[[], T_Result],
        delivery_address_company: typing.Callable[[], T_Result],
        delivery_address_company_accounting_period: typing.Callable[[], T_Result],
        delivery_address_vendor: typing.Callable[[], T_Result],
        delivery_address_vendor_accounting_period: typing.Callable[[], T_Result],
        delivery_address_vendor_company: typing.Callable[[], T_Result],
        delivery_address_vendor_company_accounting_period: typing.Callable[[], T_Result],
        line_items: typing.Callable[[], T_Result],
        line_items_accounting_period: typing.Callable[[], T_Result],
        line_items_company: typing.Callable[[], T_Result],
        line_items_company_accounting_period: typing.Callable[[], T_Result],
        line_items_delivery_address: typing.Callable[[], T_Result],
        line_items_delivery_address_accounting_period: typing.Callable[[], T_Result],
        line_items_delivery_address_company: typing.Callable[[], T_Result],
        line_items_delivery_address_company_accounting_period: typing.Callable[[], T_Result],
        line_items_delivery_address_vendor: typing.Callable[[], T_Result],
        line_items_delivery_address_vendor_accounting_period: typing.Callable[[], T_Result],
        line_items_delivery_address_vendor_company: typing.Callable[[], T_Result],
        line_items_delivery_address_vendor_company_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories: typing.Callable[[], T_Result],
        line_items_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_company_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_vendor: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_vendor_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_vendor_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_delivery_address_vendor_company_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_vendor: typing.Callable[[], T_Result],
        line_items_tracking_categories_vendor_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_vendor_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_vendor_company_accounting_period: typing.Callable[[], T_Result],
        line_items_vendor: typing.Callable[[], T_Result],
        line_items_vendor_accounting_period: typing.Callable[[], T_Result],
        line_items_vendor_company: typing.Callable[[], T_Result],
        line_items_vendor_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_delivery_address: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_company: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_vendor: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_vendor_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_vendor_company: typing.Callable[[], T_Result],
        tracking_categories_delivery_address_vendor_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_vendor: typing.Callable[[], T_Result],
        tracking_categories_vendor_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_vendor_company: typing.Callable[[], T_Result],
        tracking_categories_vendor_company_accounting_period: typing.Callable[[], T_Result],
        vendor: typing.Callable[[], T_Result],
        vendor_accounting_period: typing.Callable[[], T_Result],
        vendor_company: typing.Callable[[], T_Result],
        vendor_company_accounting_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PurchaseOrdersListRequestExpand.ACCOUNTING_PERIOD:
            return accounting_period()
        if self is PurchaseOrdersListRequestExpand.COMPANY:
            return company()
        if self is PurchaseOrdersListRequestExpand.COMPANY_ACCOUNTING_PERIOD:
            return company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS:
            return delivery_address()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_ACCOUNTING_PERIOD:
            return delivery_address_accounting_period()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_COMPANY:
            return delivery_address_company()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD:
            return delivery_address_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_VENDOR:
            return delivery_address_vendor()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD:
            return delivery_address_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_VENDOR_COMPANY:
            return delivery_address_vendor_company()
        if self is PurchaseOrdersListRequestExpand.DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD:
            return delivery_address_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS:
            return line_items()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_ACCOUNTING_PERIOD:
            return line_items_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_COMPANY:
            return line_items_company()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_COMPANY_ACCOUNTING_PERIOD:
            return line_items_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS:
            return line_items_delivery_address()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_ACCOUNTING_PERIOD:
            return line_items_delivery_address_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_COMPANY:
            return line_items_delivery_address_company()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD:
            return line_items_delivery_address_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_VENDOR:
            return line_items_delivery_address_vendor()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD:
            return line_items_delivery_address_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_VENDOR_COMPANY:
            return line_items_delivery_address_vendor_company()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD:
            return line_items_delivery_address_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES:
            return line_items_tracking_categories()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_COMPANY:
            return line_items_tracking_categories_company()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS:
            return line_items_tracking_categories_delivery_address()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_delivery_address_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY:
            return line_items_tracking_categories_delivery_address_company()
        if (
            self
            is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD
        ):
            return line_items_tracking_categories_delivery_address_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR:
            return line_items_tracking_categories_delivery_address_vendor()
        if (
            self
            is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD
        ):
            return line_items_tracking_categories_delivery_address_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY:
            return line_items_tracking_categories_delivery_address_vendor_company()
        if (
            self
            is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD
        ):
            return line_items_tracking_categories_delivery_address_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_VENDOR:
            return line_items_tracking_categories_vendor()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_VENDOR_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_VENDOR_COMPANY:
            return line_items_tracking_categories_vendor_company()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_VENDOR_COMPANY_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_VENDOR:
            return line_items_vendor()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_VENDOR_ACCOUNTING_PERIOD:
            return line_items_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_VENDOR_COMPANY:
            return line_items_vendor_company()
        if self is PurchaseOrdersListRequestExpand.LINE_ITEMS_VENDOR_COMPANY_ACCOUNTING_PERIOD:
            return line_items_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return tracking_categories_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS:
            return tracking_categories_delivery_address()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_ACCOUNTING_PERIOD:
            return tracking_categories_delivery_address_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY:
            return tracking_categories_delivery_address_company()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_delivery_address_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR:
            return tracking_categories_delivery_address_vendor()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_ACCOUNTING_PERIOD:
            return tracking_categories_delivery_address_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY:
            return tracking_categories_delivery_address_vendor_company()
        if (
            self
            is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_DELIVERY_ADDRESS_VENDOR_COMPANY_ACCOUNTING_PERIOD
        ):
            return tracking_categories_delivery_address_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_VENDOR:
            return tracking_categories_vendor()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_VENDOR_ACCOUNTING_PERIOD:
            return tracking_categories_vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_VENDOR_COMPANY:
            return tracking_categories_vendor_company()
        if self is PurchaseOrdersListRequestExpand.TRACKING_CATEGORIES_VENDOR_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_vendor_company_accounting_period()
        if self is PurchaseOrdersListRequestExpand.VENDOR:
            return vendor()
        if self is PurchaseOrdersListRequestExpand.VENDOR_ACCOUNTING_PERIOD:
            return vendor_accounting_period()
        if self is PurchaseOrdersListRequestExpand.VENDOR_COMPANY:
            return vendor_company()
        if self is PurchaseOrdersListRequestExpand.VENDOR_COMPANY_ACCOUNTING_PERIOD:
            return vendor_company_accounting_period()

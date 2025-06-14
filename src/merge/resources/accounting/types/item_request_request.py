# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .item_request_request_company import ItemRequestRequestCompany
from .item_request_request_purchase_account import ItemRequestRequestPurchaseAccount
from .item_request_request_purchase_tax_rate import ItemRequestRequestPurchaseTaxRate
from .item_request_request_sales_account import ItemRequestRequestSalesAccount
from .item_request_request_sales_tax_rate import ItemRequestRequestSalesTaxRate
from .item_request_request_status import ItemRequestRequestStatus
from .item_request_request_type import ItemRequestRequestType


class ItemRequestRequest(UncheckedBaseModel):
    """
    # The Item Object
    ### Description
    The `Item` object refers to the goods involved in a transaction.

    ### Usage Example
    Fetch from the `LIST Items` endpoint and view a company's items.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's name.
    """

    status: typing.Optional[ItemRequestRequestStatus] = pydantic.Field(default=None)
    """
    The item's status.
    
    * `ACTIVE` - ACTIVE
    * `ARCHIVED` - ARCHIVED
    """

    type: typing.Optional[ItemRequestRequestType] = pydantic.Field(default=None)
    """
    The item's type.
    
    * `INVENTORY` - INVENTORY
    * `NON_INVENTORY` - NON_INVENTORY
    * `SERVICE` - SERVICE
    * `UNKNOWN` - UNKNOWN
    """

    unit_price: typing.Optional[float] = pydantic.Field(default=None)
    """
    The item's unit price.
    """

    purchase_price: typing.Optional[float] = pydantic.Field(default=None)
    """
    The price at which the item is purchased from a vendor.
    """

    purchase_account: typing.Optional[ItemRequestRequestPurchaseAccount] = pydantic.Field(default=None)
    """
    References the default account used to record a purchase of the item.
    """

    sales_account: typing.Optional[ItemRequestRequestSalesAccount] = pydantic.Field(default=None)
    """
    References the default account used to record a sale.
    """

    company: typing.Optional[ItemRequestRequestCompany] = pydantic.Field(default=None)
    """
    The company the item belongs to.
    """

    purchase_tax_rate: typing.Optional[ItemRequestRequestPurchaseTaxRate] = pydantic.Field(default=None)
    """
    The default purchase tax rate for this item.
    """

    sales_tax_rate: typing.Optional[ItemRequestRequestSalesTaxRate] = pydantic.Field(default=None)
    """
    The default sales tax rate for this item.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

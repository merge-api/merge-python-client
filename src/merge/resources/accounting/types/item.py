# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_company import ItemCompany
from .item_purchase_account import ItemPurchaseAccount
from .item_sales_account import ItemSalesAccount
from .item_status import ItemStatus
from .remote_data import RemoteData


class Item(UniversalBaseModel):
    """
    # The Item Object

    ### Description

    The `Item` object refers to the goods involved in a transaction.

    ### Usage Example

    Fetch from the `LIST Items` endpoint and view a company's items.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    name: typing.Optional[str] = pydantic.Field()
    """
    The item's name.
    """

    status: typing.Optional[ItemStatus] = pydantic.Field()
    """
    The item's status.
    
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """

    unit_price: typing.Optional[float] = pydantic.Field()
    """
    The item's unit price.
    """

    purchase_price: typing.Optional[float] = pydantic.Field()
    """
    The price at which the item is purchased from a vendor.
    """

    purchase_account: typing.Optional[ItemPurchaseAccount] = pydantic.Field()
    """
    References the default account used to record a purchase of the item.
    """

    sales_account: typing.Optional[ItemSalesAccount] = pydantic.Field()
    """
    References the default account used to record a sale.
    """

    company: typing.Optional[ItemCompany] = pydantic.Field()
    """
    The company the item belongs to.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's item note was updated.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

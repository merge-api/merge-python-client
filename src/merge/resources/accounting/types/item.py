# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .item_company import ItemCompany
from .item_purchase_account import ItemPurchaseAccount
from .item_sales_account import ItemSalesAccount
from .item_status import ItemStatus
from .remote_data import RemoteData


class Item(pydantic.BaseModel):
    """
    # The Item Object
    ### Description
    The `Item` object refers to the goods involved in a transaction.

    ### Usage Example
    Fetch from the `LIST Items` endpoint and view a company's items.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The item's name.")
    status: typing.Optional[ItemStatus] = pydantic.Field(
        description=("The item's status.\n" "\n" "* `ACTIVE` - ACTIVE\n" "* `ARCHIVED` - ARCHIVED\n")
    )
    unit_price: typing.Optional[float] = pydantic.Field(description="The item's unit price.")
    purchase_price: typing.Optional[float] = pydantic.Field(
        description="The price at which the item is purchased from a vendor."
    )
    purchase_account: typing.Optional[ItemPurchaseAccount] = pydantic.Field(
        description="References the default account used to record a purchase of the item."
    )
    sales_account: typing.Optional[ItemSalesAccount] = pydantic.Field(
        description="References the default account used to record a sale."
    )
    company: typing.Optional[ItemCompany] = pydantic.Field(description="The company the item belongs to.")
    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's item note was updated."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

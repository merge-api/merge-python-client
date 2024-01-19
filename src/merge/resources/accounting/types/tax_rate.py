# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .tax_rate_company import TaxRateCompany

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TaxRate(pydantic.BaseModel):
    """
    # The TaxRate Object

    ### Description

    The `TaxRate` object is used to represent a tax rate.

    ### Usage Example

    Fetch from the `LIST TaxRates` endpoint and view tax rates relevant to a company.
    """

    description: typing.Optional[str] = pydantic.Field(description="The tax rate's description.")
    total_tax_rate: typing.Optional[float] = pydantic.Field(description="The tax rate's total tax rate.")
    effective_tax_rate: typing.Optional[float] = pydantic.Field(description="The tax rate's effective tax rate.")
    company: typing.Optional[TaxRateCompany] = pydantic.Field(description="The company the tax rate belongs to.")
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime]
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
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}

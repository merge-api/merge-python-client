# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_data import RemoteData
from .tax_rate_company import TaxRateCompany


class TaxRate(UniversalBaseModel):
    """
    # The TaxRate Object

    ### Description

    The `TaxRate` object is used to represent a tax rate.

    ### Usage Example

    Fetch from the `LIST TaxRates` endpoint and view tax rates relevant to a company.
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

    description: typing.Optional[str] = pydantic.Field()
    """
    The tax rate's description.
    """

    total_tax_rate: typing.Optional[float] = pydantic.Field()
    """
    The tax’s total tax rate - sum of the tax components (not compounded).
    """

    effective_tax_rate: typing.Optional[float] = pydantic.Field()
    """
    The tax rate’s effective tax rate - total amount of tax with compounding.
    """

    company: typing.Optional[TaxRateCompany] = pydantic.Field()
    """
    The subsidiary that the tax rate belongs to (in the case of multi-entity systems).
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

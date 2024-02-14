# This file was auto-generated by Fern from our API Definition.

import typing

from .address import Address
from .address_country import AddressCountry
from .address_type import AddressType
from .address_type_enum import AddressTypeEnum
from .country_enum import CountryEnum

PurchaseOrderRequestDeliveryAddress = typing.Union[str, Address]

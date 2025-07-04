# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .location_country import LocationCountry
from .location_location_type import LocationLocationType
from .remote_data import RemoteData


class Location(UncheckedBaseModel):
    """
    # The Location Object
    ### Description
    The `Location` object is used to represent an address that can be associated with an employee.

    ### Usage Example
    Fetch from the `LIST Locations` endpoint and filter by `ID` to show all office locations.
    """

    id: typing.Optional[str] = None
    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location's name.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location's phone number.
    """

    street_1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Line 1 of the location's street address.
    """

    street_2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Line 2 of the location's street address.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location's city.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location's state. Represents a region if outside of the US.
    """

    zip_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location's zip code or postal code.
    """

    country: typing.Optional[LocationCountry] = pydantic.Field(default=None)
    """
    The location's country.
    
    * `AF` - Afghanistan
    * `AX` - Åland Islands
    * `AL` - Albania
    * `DZ` - Algeria
    * `AS` - American Samoa
    * `AD` - Andorra
    * `AO` - Angola
    * `AI` - Anguilla
    * `AQ` - Antarctica
    * `AG` - Antigua and Barbuda
    * `AR` - Argentina
    * `AM` - Armenia
    * `AW` - Aruba
    * `AU` - Australia
    * `AT` - Austria
    * `AZ` - Azerbaijan
    * `BS` - Bahamas
    * `BH` - Bahrain
    * `BD` - Bangladesh
    * `BB` - Barbados
    * `BY` - Belarus
    * `BE` - Belgium
    * `BZ` - Belize
    * `BJ` - Benin
    * `BM` - Bermuda
    * `BT` - Bhutan
    * `BO` - Bolivia
    * `BQ` - Bonaire, Sint Eustatius and Saba
    * `BA` - Bosnia and Herzegovina
    * `BW` - Botswana
    * `BV` - Bouvet Island
    * `BR` - Brazil
    * `IO` - British Indian Ocean Territory
    * `BN` - Brunei
    * `BG` - Bulgaria
    * `BF` - Burkina Faso
    * `BI` - Burundi
    * `CV` - Cabo Verde
    * `KH` - Cambodia
    * `CM` - Cameroon
    * `CA` - Canada
    * `KY` - Cayman Islands
    * `CF` - Central African Republic
    * `TD` - Chad
    * `CL` - Chile
    * `CN` - China
    * `CX` - Christmas Island
    * `CC` - Cocos (Keeling) Islands
    * `CO` - Colombia
    * `KM` - Comoros
    * `CG` - Congo
    * `CD` - Congo (the Democratic Republic of the)
    * `CK` - Cook Islands
    * `CR` - Costa Rica
    * `CI` - Côte d'Ivoire
    * `HR` - Croatia
    * `CU` - Cuba
    * `CW` - Curaçao
    * `CY` - Cyprus
    * `CZ` - Czechia
    * `DK` - Denmark
    * `DJ` - Djibouti
    * `DM` - Dominica
    * `DO` - Dominican Republic
    * `EC` - Ecuador
    * `EG` - Egypt
    * `SV` - El Salvador
    * `GQ` - Equatorial Guinea
    * `ER` - Eritrea
    * `EE` - Estonia
    * `SZ` - Eswatini
    * `ET` - Ethiopia
    * `FK` - Falkland Islands (Malvinas)
    * `FO` - Faroe Islands
    * `FJ` - Fiji
    * `FI` - Finland
    * `FR` - France
    * `GF` - French Guiana
    * `PF` - French Polynesia
    * `TF` - French Southern Territories
    * `GA` - Gabon
    * `GM` - Gambia
    * `GE` - Georgia
    * `DE` - Germany
    * `GH` - Ghana
    * `GI` - Gibraltar
    * `GR` - Greece
    * `GL` - Greenland
    * `GD` - Grenada
    * `GP` - Guadeloupe
    * `GU` - Guam
    * `GT` - Guatemala
    * `GG` - Guernsey
    * `GN` - Guinea
    * `GW` - Guinea-Bissau
    * `GY` - Guyana
    * `HT` - Haiti
    * `HM` - Heard Island and McDonald Islands
    * `VA` - Holy See
    * `HN` - Honduras
    * `HK` - Hong Kong
    * `HU` - Hungary
    * `IS` - Iceland
    * `IN` - India
    * `ID` - Indonesia
    * `IR` - Iran
    * `IQ` - Iraq
    * `IE` - Ireland
    * `IM` - Isle of Man
    * `IL` - Israel
    * `IT` - Italy
    * `JM` - Jamaica
    * `JP` - Japan
    * `JE` - Jersey
    * `JO` - Jordan
    * `KZ` - Kazakhstan
    * `KE` - Kenya
    * `KI` - Kiribati
    * `KW` - Kuwait
    * `KG` - Kyrgyzstan
    * `LA` - Laos
    * `LV` - Latvia
    * `LB` - Lebanon
    * `LS` - Lesotho
    * `LR` - Liberia
    * `LY` - Libya
    * `LI` - Liechtenstein
    * `LT` - Lithuania
    * `LU` - Luxembourg
    * `MO` - Macao
    * `MG` - Madagascar
    * `MW` - Malawi
    * `MY` - Malaysia
    * `MV` - Maldives
    * `ML` - Mali
    * `MT` - Malta
    * `MH` - Marshall Islands
    * `MQ` - Martinique
    * `MR` - Mauritania
    * `MU` - Mauritius
    * `YT` - Mayotte
    * `MX` - Mexico
    * `FM` - Micronesia (Federated States of)
    * `MD` - Moldova
    * `MC` - Monaco
    * `MN` - Mongolia
    * `ME` - Montenegro
    * `MS` - Montserrat
    * `MA` - Morocco
    * `MZ` - Mozambique
    * `MM` - Myanmar
    * `NA` - Namibia
    * `NR` - Nauru
    * `NP` - Nepal
    * `NL` - Netherlands
    * `NC` - New Caledonia
    * `NZ` - New Zealand
    * `NI` - Nicaragua
    * `NE` - Niger
    * `NG` - Nigeria
    * `NU` - Niue
    * `NF` - Norfolk Island
    * `KP` - North Korea
    * `MK` - North Macedonia
    * `MP` - Northern Mariana Islands
    * `NO` - Norway
    * `OM` - Oman
    * `PK` - Pakistan
    * `PW` - Palau
    * `PS` - Palestine, State of
    * `PA` - Panama
    * `PG` - Papua New Guinea
    * `PY` - Paraguay
    * `PE` - Peru
    * `PH` - Philippines
    * `PN` - Pitcairn
    * `PL` - Poland
    * `PT` - Portugal
    * `PR` - Puerto Rico
    * `QA` - Qatar
    * `RE` - Réunion
    * `RO` - Romania
    * `RU` - Russia
    * `RW` - Rwanda
    * `BL` - Saint Barthélemy
    * `SH` - Saint Helena, Ascension and Tristan da Cunha
    * `KN` - Saint Kitts and Nevis
    * `LC` - Saint Lucia
    * `MF` - Saint Martin (French part)
    * `PM` - Saint Pierre and Miquelon
    * `VC` - Saint Vincent and the Grenadines
    * `WS` - Samoa
    * `SM` - San Marino
    * `ST` - Sao Tome and Principe
    * `SA` - Saudi Arabia
    * `SN` - Senegal
    * `RS` - Serbia
    * `SC` - Seychelles
    * `SL` - Sierra Leone
    * `SG` - Singapore
    * `SX` - Sint Maarten (Dutch part)
    * `SK` - Slovakia
    * `SI` - Slovenia
    * `SB` - Solomon Islands
    * `SO` - Somalia
    * `ZA` - South Africa
    * `GS` - South Georgia and the South Sandwich Islands
    * `KR` - South Korea
    * `SS` - South Sudan
    * `ES` - Spain
    * `LK` - Sri Lanka
    * `SD` - Sudan
    * `SR` - Suriname
    * `SJ` - Svalbard and Jan Mayen
    * `SE` - Sweden
    * `CH` - Switzerland
    * `SY` - Syria
    * `TW` - Taiwan
    * `TJ` - Tajikistan
    * `TZ` - Tanzania
    * `TH` - Thailand
    * `TL` - Timor-Leste
    * `TG` - Togo
    * `TK` - Tokelau
    * `TO` - Tonga
    * `TT` - Trinidad and Tobago
    * `TN` - Tunisia
    * `TR` - Turkey
    * `TM` - Turkmenistan
    * `TC` - Turks and Caicos Islands
    * `TV` - Tuvalu
    * `UG` - Uganda
    * `UA` - Ukraine
    * `AE` - United Arab Emirates
    * `GB` - United Kingdom
    * `UM` - United States Minor Outlying Islands
    * `US` - United States of America
    * `UY` - Uruguay
    * `UZ` - Uzbekistan
    * `VU` - Vanuatu
    * `VE` - Venezuela
    * `VN` - Vietnam
    * `VG` - Virgin Islands (British)
    * `VI` - Virgin Islands (U.S.)
    * `WF` - Wallis and Futuna
    * `EH` - Western Sahara
    * `YE` - Yemen
    * `ZM` - Zambia
    * `ZW` - Zimbabwe
    """

    location_type: typing.Optional[LocationLocationType] = pydantic.Field(default=None)
    """
    The location's type. Can be either WORK or HOME
    
    * `HOME` - HOME
    * `WORK` - WORK
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_data: typing.Optional[typing.List[RemoteData]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

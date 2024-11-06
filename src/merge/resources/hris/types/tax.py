# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Tax(UniversalBaseModel):
    """
    # The Tax Object

    ### Description

    The `Tax` object is used to represent an array of the tax deductions for a given employee's payroll run.

    ### Usage Example

    Fetch from the `LIST Taxes` endpoint and filter by `ID` to show all taxes.
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

    employee_payroll_run: typing.Optional[str] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax's name.
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The tax amount.
    """

    employer_tax: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the employer is responsible for paying the tax.
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

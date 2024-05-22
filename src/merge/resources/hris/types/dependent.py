# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .dependent_gender import DependentGender
from .dependent_relationship import DependentRelationship
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Dependent(pydantic.BaseModel):
    """
    # The Dependent Object

    ### Description

    The `Dependent` object is used to represent a dependent (e.g. child, spouse, domestic partner, etc) of an `Employee`

    ### Usage Example

    Fetch from the `LIST Dependents` endpoint and filter by `ID` to show all dependents.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was created by Merge."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was modified by Merge."
    )
    first_name: typing.Optional[str] = pydantic.Field(description="The dependents's first name.")
    middle_name: typing.Optional[str] = pydantic.Field(description="The dependents's middle name.")
    last_name: typing.Optional[str] = pydantic.Field(description="The dependents's last name.")
    relationship: typing.Optional[DependentRelationship] = pydantic.Field(
        description=(
            "The dependent's relationship to the employee.\n"
            "\n"
            "- `CHILD` - CHILD\n"
            "- `SPOUSE` - SPOUSE\n"
            "- `DOMESTIC_PARTNER` - DOMESTIC_PARTNER\n"
        )
    )
    employee: typing.Optional[str] = pydantic.Field(description="The employee this person is a dependent of.")
    date_of_birth: typing.Optional[dt.datetime] = pydantic.Field(description="The dependent's date of birth.")
    gender: typing.Optional[DependentGender] = pydantic.Field(
        description=(
            "The dependent's gender.\n"
            "\n"
            "- `MALE` - MALE\n"
            "- `FEMALE` - FEMALE\n"
            "- `NON-BINARY` - NON-BINARY\n"
            "- `OTHER` - OTHER\n"
            "- `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE\n"
        )
    )
    phone_number: typing.Optional[str] = pydantic.Field(description="The dependent's phone number.")
    home_location: typing.Optional[str] = pydantic.Field(description="The dependents's home address.")
    is_student: typing.Optional[bool] = pydantic.Field(description="Whether or not the dependent is a student")
    ssn: typing.Optional[str] = pydantic.Field(description="The dependents's social security number.")
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
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

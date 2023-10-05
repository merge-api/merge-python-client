# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .tracking_category_category_type import TrackingCategoryCategoryType
from .tracking_category_company import TrackingCategoryCompany
from .tracking_category_status import TrackingCategoryStatus


class TrackingCategory(pydantic.BaseModel):
    """
    # The TrackingCategory Object
    ### Description
    The `TrackingCategory` object is used to represent a company's tracking categories.

    ### Usage Example
    Fetch from the `GET TrackingCategory` endpoint and view a company's tracking category.
    """

    name: typing.Optional[str] = pydantic.Field(description="The tracking category's name.")
    status: typing.Optional[TrackingCategoryStatus] = pydantic.Field(
        description=("The tracking category's status.\n" "\n" "* `ACTIVE` - ACTIVE\n" "* `ARCHIVED` - ARCHIVED\n")
    )
    category_type: typing.Optional[TrackingCategoryCategoryType] = pydantic.Field(
        description=("The tracking category’s type.\n" "\n" "* `CLASS` - CLASS\n" "* `DEPARTMENT` - DEPARTMENT\n")
    )
    parent_category: typing.Optional[str] = pydantic.Field(description="ID of the parent tracking category.")
    company: typing.Optional[TrackingCategoryCompany] = pydantic.Field(
        description="The company the tracking category belongs to."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
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

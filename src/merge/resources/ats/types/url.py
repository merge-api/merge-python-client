# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .url_url_type import UrlUrlType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Url(pydantic.BaseModel):
    """
    # The Url Object

    ### Description

    The `Url` object is used to represent hyperlinks associated with the parent model.

    ### Usage Example

    Fetch from the `GET Candidate` endpoint and view their website urls.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was created by Merge."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was modified by Merge."
    )
    value: typing.Optional[str] = pydantic.Field(description="The site's url.")
    url_type: typing.Optional[UrlUrlType] = pydantic.Field(
        description=(
            "The type of site.\n"
            "\n"
            "- `PERSONAL` - PERSONAL\n"
            "- `COMPANY` - COMPANY\n"
            "- `PORTFOLIO` - PORTFOLIO\n"
            "- `BLOG` - BLOG\n"
            "- `SOCIAL_MEDIA` - SOCIAL_MEDIA\n"
            "- `OTHER` - OTHER\n"
            "- `JOB_POSTING` - JOB_POSTING\n"
        )
    )

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

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .remote_field import RemoteField
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class CustomObject(UniversalBaseModel):
    """
    # The CustomObject Object

    ### Description

    The `Custom Object` record refers to an instance of a Custom Object Class.

    ### Usage Example

    TODO
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

    object_class: typing.Optional[str] = pydantic.Field()
    """
    The custom object class the custom object record belongs to.
    """

    fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field()
    """
    The fields and values contained within the custom object record.
    """

    remote_fields: typing.Optional[typing.List[RemoteField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

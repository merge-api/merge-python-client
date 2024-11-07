# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
import pydantic
from .association_association_type import AssociationAssociationType
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Association(UniversalBaseModel):
    """
    # The Association Object

    ### Description

    The `Association` record refers to an instance of an Association Type.

    ### Usage Example

    TODO
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    source_object: typing.Optional[str] = None
    target_object: typing.Optional[str] = None
    association_type: typing.Optional[AssociationAssociationType] = pydantic.Field(default=None)
    """
    The association type the association belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

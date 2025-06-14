# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel


class ModelOperation(UncheckedBaseModel):
    """
    # The ModelOperation Object
    ### Description
    The `ModelOperation` object is used to represent the operations that are currently supported for a given model.

    ### Usage Example
    View what operations are supported for the `Candidate` endpoint.
    """

    model_name: str
    available_operations: typing.List[str]
    required_post_parameters: typing.List[str]
    supported_fields: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

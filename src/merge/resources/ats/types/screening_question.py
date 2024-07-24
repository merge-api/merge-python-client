# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .screening_question_job import ScreeningQuestionJob
from .screening_question_type import ScreeningQuestionType


class ScreeningQuestion(UniversalBaseModel):
    """
    # The ScreeningQuestion Object

    ### Description

    The `ScreeningQuestion` object is used to represent questions asked to screen candidates for a job.

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

    job: typing.Optional[ScreeningQuestionJob] = pydantic.Field()
    """
    The job associated with the screening question.
    """

    description: typing.Optional[str] = pydantic.Field()
    """
    The description of the screening question
    """

    title: typing.Optional[str] = pydantic.Field()
    """
    The title of the screening question
    """

    type: typing.Optional[ScreeningQuestionType] = pydantic.Field()
    """
    The data type for the screening question.
    
    - `DATE` - DATE
    - `FILE` - FILE
    - `SINGLE_SELECT` - SINGLE_SELECT
    - `MULTI_SELECT` - MULTI_SELECT
    - `SINGLE_LINE_TEXT` - SINGLE_LINE_TEXT
    - `MULTI_LINE_TEXT` - MULTI_LINE_TEXT
    - `NUMERIC` - NUMERIC
    - `BOOLEAN` - BOOLEAN
    """

    required: typing.Optional[bool] = pydantic.Field()
    """
    Whether or not the screening question is required.
    """

    options: typing.Optional[typing.List[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

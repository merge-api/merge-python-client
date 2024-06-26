# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .patched_task_request_status import PatchedTaskRequestStatus
from .remote_field_request import RemoteFieldRequest


class PatchedTaskRequest(pydantic_v1.BaseModel):
    """
    # The Task Object

    ### Description

    The `Task` object is used to represent a task, such as a to-do item.

    ### Usage Example

    TODO
    """

    subject: typing.Optional[str] = pydantic_v1.Field()
    """
    The task's subject.
    """

    content: typing.Optional[str] = pydantic_v1.Field()
    """
    The task's content.
    """

    owner: typing.Optional[str] = pydantic_v1.Field()
    """
    The task's owner.
    """

    account: typing.Optional[str] = pydantic_v1.Field()
    """
    The task's account.
    """

    opportunity: typing.Optional[str] = pydantic_v1.Field()
    """
    The task's opportunity.
    """

    completed_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the task is completed.
    """

    due_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the task is due.
    """

    status: typing.Optional[PatchedTaskRequestStatus] = pydantic_v1.Field()
    """
    The task's status.
    
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

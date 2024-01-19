# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .patched_task_request_status import PatchedTaskRequestStatus
from .remote_field_request import RemoteFieldRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PatchedTaskRequest(pydantic.BaseModel):
    """
    # The Task Object

    ### Description

    The `Task` object is used to represent a task, such as a to-do item.

    ### Usage Example

    TODO
    """

    subject: typing.Optional[str] = pydantic.Field(description="The task's subject.")
    content: typing.Optional[str] = pydantic.Field(description="The task's content.")
    owner: typing.Optional[str] = pydantic.Field(description="The task's owner.")
    account: typing.Optional[str] = pydantic.Field(description="The task's account.")
    opportunity: typing.Optional[str] = pydantic.Field(description="The task's opportunity.")
    completed_date: typing.Optional[dt.datetime] = pydantic.Field(description="When the task is completed.")
    due_date: typing.Optional[dt.datetime] = pydantic.Field(description="When the task is due.")
    status: typing.Optional[PatchedTaskRequestStatus] = pydantic.Field(
        description=("The task's status.\n" "\n" "- `OPEN` - OPEN\n" "- `CLOSED` - CLOSED\n")
    )
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

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

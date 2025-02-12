# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CollectionsListRequestExpand(str, enum.Enum):
    PARENT_COLLECTION = "parent_collection"
    TEAMS = "teams"
    TEAMS_PARENT_COLLECTION = "teams,parent_collection"

    def visit(
        self,
        parent_collection: typing.Callable[[], T_Result],
        teams: typing.Callable[[], T_Result],
        teams_parent_collection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CollectionsListRequestExpand.PARENT_COLLECTION:
            return parent_collection()
        if self is CollectionsListRequestExpand.TEAMS:
            return teams()
        if self is CollectionsListRequestExpand.TEAMS_PARENT_COLLECTION:
            return teams_parent_collection()

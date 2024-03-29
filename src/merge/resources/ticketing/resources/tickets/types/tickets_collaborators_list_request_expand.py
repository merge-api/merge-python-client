# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TicketsCollaboratorsListRequestExpand(str, enum.Enum):
    ROLES = "roles"
    TEAMS = "teams"
    TEAMS_ROLES = "teams,roles"

    def visit(
        self,
        roles: typing.Callable[[], T_Result],
        teams: typing.Callable[[], T_Result],
        teams_roles: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TicketsCollaboratorsListRequestExpand.ROLES:
            return roles()
        if self is TicketsCollaboratorsListRequestExpand.TEAMS:
            return teams()
        if self is TicketsCollaboratorsListRequestExpand.TEAMS_ROLES:
            return teams_roles()

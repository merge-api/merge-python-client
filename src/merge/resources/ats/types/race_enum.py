# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RaceEnum(str, enum.Enum):
    """
    * `AMERICAN_INDIAN_OR_ALASKAN_NATIVE` - AMERICAN_INDIAN_OR_ALASKAN_NATIVE
    * `ASIAN` - ASIAN
    * `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN
    * `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO
    * `WHITE` - WHITE
    * `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER
    * `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES
    * `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY
    """

    AMERICAN_INDIAN_OR_ALASKAN_NATIVE = "AMERICAN_INDIAN_OR_ALASKAN_NATIVE"
    ASIAN = "ASIAN"
    BLACK_OR_AFRICAN_AMERICAN = "BLACK_OR_AFRICAN_AMERICAN"
    HISPANIC_OR_LATINO = "HISPANIC_OR_LATINO"
    WHITE = "WHITE"
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER"
    TWO_OR_MORE_RACES = "TWO_OR_MORE_RACES"
    DECLINE_TO_SELF_IDENTIFY = "DECLINE_TO_SELF_IDENTIFY"

    def visit(
        self,
        american_indian_or_alaskan_native: typing.Callable[[], T_Result],
        asian: typing.Callable[[], T_Result],
        black_or_african_american: typing.Callable[[], T_Result],
        hispanic_or_latino: typing.Callable[[], T_Result],
        white: typing.Callable[[], T_Result],
        native_hawaiian_or_other_pacific_islander: typing.Callable[[], T_Result],
        two_or_more_races: typing.Callable[[], T_Result],
        decline_to_self_identify: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RaceEnum.AMERICAN_INDIAN_OR_ALASKAN_NATIVE:
            return american_indian_or_alaskan_native()
        if self is RaceEnum.ASIAN:
            return asian()
        if self is RaceEnum.BLACK_OR_AFRICAN_AMERICAN:
            return black_or_african_american()
        if self is RaceEnum.HISPANIC_OR_LATINO:
            return hispanic_or_latino()
        if self is RaceEnum.WHITE:
            return white()
        if self is RaceEnum.NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER:
            return native_hawaiian_or_other_pacific_islander()
        if self is RaceEnum.TWO_OR_MORE_RACES:
            return two_or_more_races()
        if self is RaceEnum.DECLINE_TO_SELF_IDENTIFY:
            return decline_to_self_identify()
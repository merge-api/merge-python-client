# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmploymentsRetrieveRequestShowEnumOrigins(str, enum.Enum):
    EMPLOYMENT_TYPE = "employment_type"
    EMPLOYMENT_TYPE_FLSA_STATUS = "employment_type,flsa_status"
    EMPLOYMENT_TYPE_FLSA_STATUS_PAY_FREQUENCY = "employment_type,flsa_status,pay_frequency"
    EMPLOYMENT_TYPE_FLSA_STATUS_PAY_FREQUENCY_PAY_PERIOD = "employment_type,flsa_status,pay_frequency,pay_period"
    EMPLOYMENT_TYPE_FLSA_STATUS_PAY_PERIOD = "employment_type,flsa_status,pay_period"
    EMPLOYMENT_TYPE_PAY_FREQUENCY = "employment_type,pay_frequency"
    EMPLOYMENT_TYPE_PAY_FREQUENCY_PAY_PERIOD = "employment_type,pay_frequency,pay_period"
    EMPLOYMENT_TYPE_PAY_PERIOD = "employment_type,pay_period"
    FLSA_STATUS = "flsa_status"
    FLSA_STATUS_PAY_FREQUENCY = "flsa_status,pay_frequency"
    FLSA_STATUS_PAY_FREQUENCY_PAY_PERIOD = "flsa_status,pay_frequency,pay_period"
    FLSA_STATUS_PAY_PERIOD = "flsa_status,pay_period"
    PAY_FREQUENCY = "pay_frequency"
    PAY_FREQUENCY_PAY_PERIOD = "pay_frequency,pay_period"
    PAY_PERIOD = "pay_period"

    def visit(
        self,
        employment_type: typing.Callable[[], T_Result],
        employment_type_flsa_status: typing.Callable[[], T_Result],
        employment_type_flsa_status_pay_frequency: typing.Callable[[], T_Result],
        employment_type_flsa_status_pay_frequency_pay_period: typing.Callable[[], T_Result],
        employment_type_flsa_status_pay_period: typing.Callable[[], T_Result],
        employment_type_pay_frequency: typing.Callable[[], T_Result],
        employment_type_pay_frequency_pay_period: typing.Callable[[], T_Result],
        employment_type_pay_period: typing.Callable[[], T_Result],
        flsa_status: typing.Callable[[], T_Result],
        flsa_status_pay_frequency: typing.Callable[[], T_Result],
        flsa_status_pay_frequency_pay_period: typing.Callable[[], T_Result],
        flsa_status_pay_period: typing.Callable[[], T_Result],
        pay_frequency: typing.Callable[[], T_Result],
        pay_frequency_pay_period: typing.Callable[[], T_Result],
        pay_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE:
            return employment_type()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_FLSA_STATUS:
            return employment_type_flsa_status()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_FLSA_STATUS_PAY_FREQUENCY:
            return employment_type_flsa_status_pay_frequency()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_FLSA_STATUS_PAY_FREQUENCY_PAY_PERIOD:
            return employment_type_flsa_status_pay_frequency_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_FLSA_STATUS_PAY_PERIOD:
            return employment_type_flsa_status_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_PAY_FREQUENCY:
            return employment_type_pay_frequency()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_PAY_FREQUENCY_PAY_PERIOD:
            return employment_type_pay_frequency_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.EMPLOYMENT_TYPE_PAY_PERIOD:
            return employment_type_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.FLSA_STATUS:
            return flsa_status()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.FLSA_STATUS_PAY_FREQUENCY:
            return flsa_status_pay_frequency()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.FLSA_STATUS_PAY_FREQUENCY_PAY_PERIOD:
            return flsa_status_pay_frequency_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.FLSA_STATUS_PAY_PERIOD:
            return flsa_status_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.PAY_FREQUENCY:
            return pay_frequency()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.PAY_FREQUENCY_PAY_PERIOD:
            return pay_frequency_pay_period()
        if self is EmploymentsRetrieveRequestShowEnumOrigins.PAY_PERIOD:
            return pay_period()

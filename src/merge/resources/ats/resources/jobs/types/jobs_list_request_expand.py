# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobsListRequestExpand(str, enum.Enum):
    DEPARTMENTS = "departments"
    DEPARTMENTS_HIRING_MANAGERS = "departments,hiring_managers"
    DEPARTMENTS_HIRING_MANAGERS_JOB_POSTINGS = "departments,hiring_managers,job_postings"
    DEPARTMENTS_HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS = "departments,hiring_managers,job_postings,recruiters"
    DEPARTMENTS_HIRING_MANAGERS_RECRUITERS = "departments,hiring_managers,recruiters"
    DEPARTMENTS_JOB_POSTINGS = "departments,job_postings"
    DEPARTMENTS_JOB_POSTINGS_RECRUITERS = "departments,job_postings,recruiters"
    DEPARTMENTS_OFFICES = "departments,offices"
    DEPARTMENTS_OFFICES_HIRING_MANAGERS = "departments,offices,hiring_managers"
    DEPARTMENTS_OFFICES_HIRING_MANAGERS_JOB_POSTINGS = "departments,offices,hiring_managers,job_postings"
    DEPARTMENTS_OFFICES_HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS = (
        "departments,offices,hiring_managers,job_postings,recruiters"
    )
    DEPARTMENTS_OFFICES_HIRING_MANAGERS_RECRUITERS = "departments,offices,hiring_managers,recruiters"
    DEPARTMENTS_OFFICES_JOB_POSTINGS = "departments,offices,job_postings"
    DEPARTMENTS_OFFICES_JOB_POSTINGS_RECRUITERS = "departments,offices,job_postings,recruiters"
    DEPARTMENTS_OFFICES_RECRUITERS = "departments,offices,recruiters"
    DEPARTMENTS_RECRUITERS = "departments,recruiters"
    HIRING_MANAGERS = "hiring_managers"
    HIRING_MANAGERS_JOB_POSTINGS = "hiring_managers,job_postings"
    HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS = "hiring_managers,job_postings,recruiters"
    HIRING_MANAGERS_RECRUITERS = "hiring_managers,recruiters"
    JOB_POSTINGS = "job_postings"
    JOB_POSTINGS_RECRUITERS = "job_postings,recruiters"
    OFFICES = "offices"
    OFFICES_HIRING_MANAGERS = "offices,hiring_managers"
    OFFICES_HIRING_MANAGERS_JOB_POSTINGS = "offices,hiring_managers,job_postings"
    OFFICES_HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS = "offices,hiring_managers,job_postings,recruiters"
    OFFICES_HIRING_MANAGERS_RECRUITERS = "offices,hiring_managers,recruiters"
    OFFICES_JOB_POSTINGS = "offices,job_postings"
    OFFICES_JOB_POSTINGS_RECRUITERS = "offices,job_postings,recruiters"
    OFFICES_RECRUITERS = "offices,recruiters"
    RECRUITERS = "recruiters"

    def visit(
        self,
        departments: typing.Callable[[], T_Result],
        departments_hiring_managers: typing.Callable[[], T_Result],
        departments_hiring_managers_job_postings: typing.Callable[[], T_Result],
        departments_hiring_managers_job_postings_recruiters: typing.Callable[[], T_Result],
        departments_hiring_managers_recruiters: typing.Callable[[], T_Result],
        departments_job_postings: typing.Callable[[], T_Result],
        departments_job_postings_recruiters: typing.Callable[[], T_Result],
        departments_offices: typing.Callable[[], T_Result],
        departments_offices_hiring_managers: typing.Callable[[], T_Result],
        departments_offices_hiring_managers_job_postings: typing.Callable[[], T_Result],
        departments_offices_hiring_managers_job_postings_recruiters: typing.Callable[[], T_Result],
        departments_offices_hiring_managers_recruiters: typing.Callable[[], T_Result],
        departments_offices_job_postings: typing.Callable[[], T_Result],
        departments_offices_job_postings_recruiters: typing.Callable[[], T_Result],
        departments_offices_recruiters: typing.Callable[[], T_Result],
        departments_recruiters: typing.Callable[[], T_Result],
        hiring_managers: typing.Callable[[], T_Result],
        hiring_managers_job_postings: typing.Callable[[], T_Result],
        hiring_managers_job_postings_recruiters: typing.Callable[[], T_Result],
        hiring_managers_recruiters: typing.Callable[[], T_Result],
        job_postings: typing.Callable[[], T_Result],
        job_postings_recruiters: typing.Callable[[], T_Result],
        offices: typing.Callable[[], T_Result],
        offices_hiring_managers: typing.Callable[[], T_Result],
        offices_hiring_managers_job_postings: typing.Callable[[], T_Result],
        offices_hiring_managers_job_postings_recruiters: typing.Callable[[], T_Result],
        offices_hiring_managers_recruiters: typing.Callable[[], T_Result],
        offices_job_postings: typing.Callable[[], T_Result],
        offices_job_postings_recruiters: typing.Callable[[], T_Result],
        offices_recruiters: typing.Callable[[], T_Result],
        recruiters: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobsListRequestExpand.DEPARTMENTS:
            return departments()
        if self is JobsListRequestExpand.DEPARTMENTS_HIRING_MANAGERS:
            return departments_hiring_managers()
        if self is JobsListRequestExpand.DEPARTMENTS_HIRING_MANAGERS_JOB_POSTINGS:
            return departments_hiring_managers_job_postings()
        if self is JobsListRequestExpand.DEPARTMENTS_HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS:
            return departments_hiring_managers_job_postings_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_HIRING_MANAGERS_RECRUITERS:
            return departments_hiring_managers_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_JOB_POSTINGS:
            return departments_job_postings()
        if self is JobsListRequestExpand.DEPARTMENTS_JOB_POSTINGS_RECRUITERS:
            return departments_job_postings_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES:
            return departments_offices()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_HIRING_MANAGERS:
            return departments_offices_hiring_managers()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_HIRING_MANAGERS_JOB_POSTINGS:
            return departments_offices_hiring_managers_job_postings()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS:
            return departments_offices_hiring_managers_job_postings_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_HIRING_MANAGERS_RECRUITERS:
            return departments_offices_hiring_managers_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_JOB_POSTINGS:
            return departments_offices_job_postings()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_JOB_POSTINGS_RECRUITERS:
            return departments_offices_job_postings_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_OFFICES_RECRUITERS:
            return departments_offices_recruiters()
        if self is JobsListRequestExpand.DEPARTMENTS_RECRUITERS:
            return departments_recruiters()
        if self is JobsListRequestExpand.HIRING_MANAGERS:
            return hiring_managers()
        if self is JobsListRequestExpand.HIRING_MANAGERS_JOB_POSTINGS:
            return hiring_managers_job_postings()
        if self is JobsListRequestExpand.HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS:
            return hiring_managers_job_postings_recruiters()
        if self is JobsListRequestExpand.HIRING_MANAGERS_RECRUITERS:
            return hiring_managers_recruiters()
        if self is JobsListRequestExpand.JOB_POSTINGS:
            return job_postings()
        if self is JobsListRequestExpand.JOB_POSTINGS_RECRUITERS:
            return job_postings_recruiters()
        if self is JobsListRequestExpand.OFFICES:
            return offices()
        if self is JobsListRequestExpand.OFFICES_HIRING_MANAGERS:
            return offices_hiring_managers()
        if self is JobsListRequestExpand.OFFICES_HIRING_MANAGERS_JOB_POSTINGS:
            return offices_hiring_managers_job_postings()
        if self is JobsListRequestExpand.OFFICES_HIRING_MANAGERS_JOB_POSTINGS_RECRUITERS:
            return offices_hiring_managers_job_postings_recruiters()
        if self is JobsListRequestExpand.OFFICES_HIRING_MANAGERS_RECRUITERS:
            return offices_hiring_managers_recruiters()
        if self is JobsListRequestExpand.OFFICES_JOB_POSTINGS:
            return offices_job_postings()
        if self is JobsListRequestExpand.OFFICES_JOB_POSTINGS_RECRUITERS:
            return offices_job_postings_recruiters()
        if self is JobsListRequestExpand.OFFICES_RECRUITERS:
            return offices_recruiters()
        if self is JobsListRequestExpand.RECRUITERS:
            return recruiters()

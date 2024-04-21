# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ApplicationsListRequestExpand(str, enum.Enum):
    CANDIDATE = "candidate"
    CANDIDATE_CREDITED_TO = "candidate,credited_to"
    CANDIDATE_CREDITED_TO_CURRENT_STAGE = "candidate,credited_to,current_stage"
    CANDIDATE_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = "candidate,credited_to,current_stage,reject_reason"
    CANDIDATE_CREDITED_TO_REJECT_REASON = "candidate,credited_to,reject_reason"
    CANDIDATE_CURRENT_STAGE = "candidate,current_stage"
    CANDIDATE_CURRENT_STAGE_REJECT_REASON = "candidate,current_stage,reject_reason"
    CANDIDATE_JOB = "candidate,job"
    CANDIDATE_JOB_CREDITED_TO = "candidate,job,credited_to"
    CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE = "candidate,job,credited_to,current_stage"
    CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = "candidate,job,credited_to,current_stage,reject_reason"
    CANDIDATE_JOB_CREDITED_TO_REJECT_REASON = "candidate,job,credited_to,reject_reason"
    CANDIDATE_JOB_CURRENT_STAGE = "candidate,job,current_stage"
    CANDIDATE_JOB_CURRENT_STAGE_REJECT_REASON = "candidate,job,current_stage,reject_reason"
    CANDIDATE_JOB_REJECT_REASON = "candidate,job,reject_reason"
    CANDIDATE_REJECT_REASON = "candidate,reject_reason"
    CREDITED_TO = "credited_to"
    CREDITED_TO_CURRENT_STAGE = "credited_to,current_stage"
    CREDITED_TO_CURRENT_STAGE_REJECT_REASON = "credited_to,current_stage,reject_reason"
    CREDITED_TO_REJECT_REASON = "credited_to,reject_reason"
    CURRENT_STAGE = "current_stage"
    CURRENT_STAGE_REJECT_REASON = "current_stage,reject_reason"
    JOB = "job"
    JOB_CREDITED_TO = "job,credited_to"
    JOB_CREDITED_TO_CURRENT_STAGE = "job,credited_to,current_stage"
    JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = "job,credited_to,current_stage,reject_reason"
    JOB_CREDITED_TO_REJECT_REASON = "job,credited_to,reject_reason"
    JOB_CURRENT_STAGE = "job,current_stage"
    JOB_CURRENT_STAGE_REJECT_REASON = "job,current_stage,reject_reason"
    JOB_REJECT_REASON = "job,reject_reason"
    OFFERS = "offers"
    OFFERS_CANDIDATE = "offers,candidate"
    OFFERS_CANDIDATE_CREDITED_TO = "offers,candidate,credited_to"
    OFFERS_CANDIDATE_CREDITED_TO_CURRENT_STAGE = "offers,candidate,credited_to,current_stage"
    OFFERS_CANDIDATE_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = (
        "offers,candidate,credited_to,current_stage,reject_reason"
    )
    OFFERS_CANDIDATE_CREDITED_TO_REJECT_REASON = "offers,candidate,credited_to,reject_reason"
    OFFERS_CANDIDATE_CURRENT_STAGE = "offers,candidate,current_stage"
    OFFERS_CANDIDATE_CURRENT_STAGE_REJECT_REASON = "offers,candidate,current_stage,reject_reason"
    OFFERS_CANDIDATE_JOB = "offers,candidate,job"
    OFFERS_CANDIDATE_JOB_CREDITED_TO = "offers,candidate,job,credited_to"
    OFFERS_CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE = "offers,candidate,job,credited_to,current_stage"
    OFFERS_CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = (
        "offers,candidate,job,credited_to,current_stage,reject_reason"
    )
    OFFERS_CANDIDATE_JOB_CREDITED_TO_REJECT_REASON = "offers,candidate,job,credited_to,reject_reason"
    OFFERS_CANDIDATE_JOB_CURRENT_STAGE = "offers,candidate,job,current_stage"
    OFFERS_CANDIDATE_JOB_CURRENT_STAGE_REJECT_REASON = "offers,candidate,job,current_stage,reject_reason"
    OFFERS_CANDIDATE_JOB_REJECT_REASON = "offers,candidate,job,reject_reason"
    OFFERS_CANDIDATE_REJECT_REASON = "offers,candidate,reject_reason"
    OFFERS_CREDITED_TO = "offers,credited_to"
    OFFERS_CREDITED_TO_CURRENT_STAGE = "offers,credited_to,current_stage"
    OFFERS_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = "offers,credited_to,current_stage,reject_reason"
    OFFERS_CREDITED_TO_REJECT_REASON = "offers,credited_to,reject_reason"
    OFFERS_CURRENT_STAGE = "offers,current_stage"
    OFFERS_CURRENT_STAGE_REJECT_REASON = "offers,current_stage,reject_reason"
    OFFERS_JOB = "offers,job"
    OFFERS_JOB_CREDITED_TO = "offers,job,credited_to"
    OFFERS_JOB_CREDITED_TO_CURRENT_STAGE = "offers,job,credited_to,current_stage"
    OFFERS_JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON = "offers,job,credited_to,current_stage,reject_reason"
    OFFERS_JOB_CREDITED_TO_REJECT_REASON = "offers,job,credited_to,reject_reason"
    OFFERS_JOB_CURRENT_STAGE = "offers,job,current_stage"
    OFFERS_JOB_CURRENT_STAGE_REJECT_REASON = "offers,job,current_stage,reject_reason"
    OFFERS_JOB_REJECT_REASON = "offers,job,reject_reason"
    OFFERS_REJECT_REASON = "offers,reject_reason"
    REJECT_REASON = "reject_reason"

    def visit(
        self,
        candidate: typing.Callable[[], T_Result],
        candidate_credited_to: typing.Callable[[], T_Result],
        candidate_credited_to_current_stage: typing.Callable[[], T_Result],
        candidate_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        candidate_credited_to_reject_reason: typing.Callable[[], T_Result],
        candidate_current_stage: typing.Callable[[], T_Result],
        candidate_current_stage_reject_reason: typing.Callable[[], T_Result],
        candidate_job: typing.Callable[[], T_Result],
        candidate_job_credited_to: typing.Callable[[], T_Result],
        candidate_job_credited_to_current_stage: typing.Callable[[], T_Result],
        candidate_job_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        candidate_job_credited_to_reject_reason: typing.Callable[[], T_Result],
        candidate_job_current_stage: typing.Callable[[], T_Result],
        candidate_job_current_stage_reject_reason: typing.Callable[[], T_Result],
        candidate_job_reject_reason: typing.Callable[[], T_Result],
        candidate_reject_reason: typing.Callable[[], T_Result],
        credited_to: typing.Callable[[], T_Result],
        credited_to_current_stage: typing.Callable[[], T_Result],
        credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        credited_to_reject_reason: typing.Callable[[], T_Result],
        current_stage: typing.Callable[[], T_Result],
        current_stage_reject_reason: typing.Callable[[], T_Result],
        job: typing.Callable[[], T_Result],
        job_credited_to: typing.Callable[[], T_Result],
        job_credited_to_current_stage: typing.Callable[[], T_Result],
        job_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        job_credited_to_reject_reason: typing.Callable[[], T_Result],
        job_current_stage: typing.Callable[[], T_Result],
        job_current_stage_reject_reason: typing.Callable[[], T_Result],
        job_reject_reason: typing.Callable[[], T_Result],
        offers: typing.Callable[[], T_Result],
        offers_candidate: typing.Callable[[], T_Result],
        offers_candidate_credited_to: typing.Callable[[], T_Result],
        offers_candidate_credited_to_current_stage: typing.Callable[[], T_Result],
        offers_candidate_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_credited_to_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_current_stage: typing.Callable[[], T_Result],
        offers_candidate_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_job: typing.Callable[[], T_Result],
        offers_candidate_job_credited_to: typing.Callable[[], T_Result],
        offers_candidate_job_credited_to_current_stage: typing.Callable[[], T_Result],
        offers_candidate_job_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_job_credited_to_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_job_current_stage: typing.Callable[[], T_Result],
        offers_candidate_job_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_job_reject_reason: typing.Callable[[], T_Result],
        offers_candidate_reject_reason: typing.Callable[[], T_Result],
        offers_credited_to: typing.Callable[[], T_Result],
        offers_credited_to_current_stage: typing.Callable[[], T_Result],
        offers_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_credited_to_reject_reason: typing.Callable[[], T_Result],
        offers_current_stage: typing.Callable[[], T_Result],
        offers_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_job: typing.Callable[[], T_Result],
        offers_job_credited_to: typing.Callable[[], T_Result],
        offers_job_credited_to_current_stage: typing.Callable[[], T_Result],
        offers_job_credited_to_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_job_credited_to_reject_reason: typing.Callable[[], T_Result],
        offers_job_current_stage: typing.Callable[[], T_Result],
        offers_job_current_stage_reject_reason: typing.Callable[[], T_Result],
        offers_job_reject_reason: typing.Callable[[], T_Result],
        offers_reject_reason: typing.Callable[[], T_Result],
        reject_reason: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplicationsListRequestExpand.CANDIDATE:
            return candidate()
        if self is ApplicationsListRequestExpand.CANDIDATE_CREDITED_TO:
            return candidate_credited_to()
        if self is ApplicationsListRequestExpand.CANDIDATE_CREDITED_TO_CURRENT_STAGE:
            return candidate_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.CANDIDATE_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return candidate_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_CREDITED_TO_REJECT_REASON:
            return candidate_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_CURRENT_STAGE:
            return candidate_current_stage()
        if self is ApplicationsListRequestExpand.CANDIDATE_CURRENT_STAGE_REJECT_REASON:
            return candidate_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB:
            return candidate_job()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_CREDITED_TO:
            return candidate_job_credited_to()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE:
            return candidate_job_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return candidate_job_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_CREDITED_TO_REJECT_REASON:
            return candidate_job_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_CURRENT_STAGE:
            return candidate_job_current_stage()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_CURRENT_STAGE_REJECT_REASON:
            return candidate_job_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_JOB_REJECT_REASON:
            return candidate_job_reject_reason()
        if self is ApplicationsListRequestExpand.CANDIDATE_REJECT_REASON:
            return candidate_reject_reason()
        if self is ApplicationsListRequestExpand.CREDITED_TO:
            return credited_to()
        if self is ApplicationsListRequestExpand.CREDITED_TO_CURRENT_STAGE:
            return credited_to_current_stage()
        if self is ApplicationsListRequestExpand.CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.CREDITED_TO_REJECT_REASON:
            return credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.CURRENT_STAGE:
            return current_stage()
        if self is ApplicationsListRequestExpand.CURRENT_STAGE_REJECT_REASON:
            return current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.JOB:
            return job()
        if self is ApplicationsListRequestExpand.JOB_CREDITED_TO:
            return job_credited_to()
        if self is ApplicationsListRequestExpand.JOB_CREDITED_TO_CURRENT_STAGE:
            return job_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return job_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.JOB_CREDITED_TO_REJECT_REASON:
            return job_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.JOB_CURRENT_STAGE:
            return job_current_stage()
        if self is ApplicationsListRequestExpand.JOB_CURRENT_STAGE_REJECT_REASON:
            return job_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.JOB_REJECT_REASON:
            return job_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS:
            return offers()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE:
            return offers_candidate()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_CREDITED_TO:
            return offers_candidate_credited_to()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_CREDITED_TO_CURRENT_STAGE:
            return offers_candidate_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return offers_candidate_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_CREDITED_TO_REJECT_REASON:
            return offers_candidate_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_CURRENT_STAGE:
            return offers_candidate_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_CURRENT_STAGE_REJECT_REASON:
            return offers_candidate_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB:
            return offers_candidate_job()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_CREDITED_TO:
            return offers_candidate_job_credited_to()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE:
            return offers_candidate_job_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return offers_candidate_job_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_CREDITED_TO_REJECT_REASON:
            return offers_candidate_job_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_CURRENT_STAGE:
            return offers_candidate_job_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_CURRENT_STAGE_REJECT_REASON:
            return offers_candidate_job_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_JOB_REJECT_REASON:
            return offers_candidate_job_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CANDIDATE_REJECT_REASON:
            return offers_candidate_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CREDITED_TO:
            return offers_credited_to()
        if self is ApplicationsListRequestExpand.OFFERS_CREDITED_TO_CURRENT_STAGE:
            return offers_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return offers_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CREDITED_TO_REJECT_REASON:
            return offers_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_CURRENT_STAGE:
            return offers_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_CURRENT_STAGE_REJECT_REASON:
            return offers_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_JOB:
            return offers_job()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_CREDITED_TO:
            return offers_job_credited_to()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_CREDITED_TO_CURRENT_STAGE:
            return offers_job_credited_to_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_CREDITED_TO_CURRENT_STAGE_REJECT_REASON:
            return offers_job_credited_to_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_CREDITED_TO_REJECT_REASON:
            return offers_job_credited_to_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_CURRENT_STAGE:
            return offers_job_current_stage()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_CURRENT_STAGE_REJECT_REASON:
            return offers_job_current_stage_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_JOB_REJECT_REASON:
            return offers_job_reject_reason()
        if self is ApplicationsListRequestExpand.OFFERS_REJECT_REASON:
            return offers_reject_reason()
        if self is ApplicationsListRequestExpand.REJECT_REASON:
            return reject_reason()

# File generated from our OpenAPI spec by Stainless.


from ..._models import BaseModel

__all__ = ["DebugLog", "LogSummary"]


class LogSummary(BaseModel):
    method: str

    status_code: int

    url: str


class DebugLog(BaseModel):
    dashboard_view: str

    log_id: str

    log_summary: LogSummary

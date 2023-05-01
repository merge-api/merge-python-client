# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DebugLog", "LogSummary"]


class LogSummary(TypedDict, total=False):
    method: Required[str]

    status_code: Required[int]

    url: Required[str]


class DebugLog(TypedDict, total=False):
    dashboard_view: Required[str]

    log_id: Required[str]

    log_summary: Required[LogSummary]

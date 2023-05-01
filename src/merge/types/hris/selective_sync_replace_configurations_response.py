# File generated from our OpenAPI spec by Stainless.

from typing import List

from ...types.shared import linked_account_selective_sync_configuration

__all__ = ["SelectiveSyncReplaceConfigurationsResponse"]

SelectiveSyncReplaceConfigurationsResponse = List[
    linked_account_selective_sync_configuration.LinkedAccountSelectiveSyncConfiguration
]

# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EventTypeEnum(str, enum.Enum):
    """
    - `CREATED_REMOTE_PRODUCTION_API_KEY` - CREATED_REMOTE_PRODUCTION_API_KEY
    - `DELETED_REMOTE_PRODUCTION_API_KEY` - DELETED_REMOTE_PRODUCTION_API_KEY
    - `CREATED_TEST_API_KEY` - CREATED_TEST_API_KEY
    - `DELETED_TEST_API_KEY` - DELETED_TEST_API_KEY
    - `REGENERATED_PRODUCTION_API_KEY` - REGENERATED_PRODUCTION_API_KEY
    - `INVITED_USER` - INVITED_USER
    - `TWO_FACTOR_AUTH_ENABLED` - TWO_FACTOR_AUTH_ENABLED
    - `TWO_FACTOR_AUTH_DISABLED` - TWO_FACTOR_AUTH_DISABLED
    - `DELETED_LINKED_ACCOUNT` - DELETED_LINKED_ACCOUNT
    - `CREATED_DESTINATION` - CREATED_DESTINATION
    - `DELETED_DESTINATION` - DELETED_DESTINATION
    - `CHANGED_DESTINATION` - CHANGED_DESTINATION
    - `CHANGED_SCOPES` - CHANGED_SCOPES
    - `CHANGED_PERSONAL_INFORMATION` - CHANGED_PERSONAL_INFORMATION
    - `CHANGED_ORGANIZATION_SETTINGS` - CHANGED_ORGANIZATION_SETTINGS
    - `ENABLED_INTEGRATION` - ENABLED_INTEGRATION
    - `DISABLED_INTEGRATION` - DISABLED_INTEGRATION
    - `ENABLED_CATEGORY` - ENABLED_CATEGORY
    - `DISABLED_CATEGORY` - DISABLED_CATEGORY
    - `CHANGED_PASSWORD` - CHANGED_PASSWORD
    - `RESET_PASSWORD` - RESET_PASSWORD
    - `ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION` - ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION
    - `ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT` - ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT
    - `DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION` - DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION
    - `DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT` - DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT
    - `CREATED_INTEGRATION_WIDE_FIELD_MAPPING` - CREATED_INTEGRATION_WIDE_FIELD_MAPPING
    - `CREATED_LINKED_ACCOUNT_FIELD_MAPPING` - CREATED_LINKED_ACCOUNT_FIELD_MAPPING
    - `CHANGED_INTEGRATION_WIDE_FIELD_MAPPING` - CHANGED_INTEGRATION_WIDE_FIELD_MAPPING
    - `CHANGED_LINKED_ACCOUNT_FIELD_MAPPING` - CHANGED_LINKED_ACCOUNT_FIELD_MAPPING
    - `DELETED_INTEGRATION_WIDE_FIELD_MAPPING` - DELETED_INTEGRATION_WIDE_FIELD_MAPPING
    - `DELETED_LINKED_ACCOUNT_FIELD_MAPPING` - DELETED_LINKED_ACCOUNT_FIELD_MAPPING
    - `FORCED_LINKED_ACCOUNT_RESYNC` - FORCED_LINKED_ACCOUNT_RESYNC
    - `MUTED_ISSUE` - MUTED_ISSUE
    - `GENERATED_MAGIC_LINK` - GENERATED_MAGIC_LINK
    - `ENABLED_MERGE_WEBHOOK` - ENABLED_MERGE_WEBHOOK
    - `DISABLED_MERGE_WEBHOOK` - DISABLED_MERGE_WEBHOOK
    - `MERGE_WEBHOOK_TARGET_CHANGED` - MERGE_WEBHOOK_TARGET_CHANGED
    - `END_USER_CREDENTIALS_ACCESSED` - END_USER_CREDENTIALS_ACCESSED
    """

    CREATED_REMOTE_PRODUCTION_API_KEY = "CREATED_REMOTE_PRODUCTION_API_KEY"
    DELETED_REMOTE_PRODUCTION_API_KEY = "DELETED_REMOTE_PRODUCTION_API_KEY"
    CREATED_TEST_API_KEY = "CREATED_TEST_API_KEY"
    DELETED_TEST_API_KEY = "DELETED_TEST_API_KEY"
    REGENERATED_PRODUCTION_API_KEY = "REGENERATED_PRODUCTION_API_KEY"
    INVITED_USER = "INVITED_USER"
    TWO_FACTOR_AUTH_ENABLED = "TWO_FACTOR_AUTH_ENABLED"
    TWO_FACTOR_AUTH_DISABLED = "TWO_FACTOR_AUTH_DISABLED"
    DELETED_LINKED_ACCOUNT = "DELETED_LINKED_ACCOUNT"
    CREATED_DESTINATION = "CREATED_DESTINATION"
    DELETED_DESTINATION = "DELETED_DESTINATION"
    CHANGED_DESTINATION = "CHANGED_DESTINATION"
    CHANGED_SCOPES = "CHANGED_SCOPES"
    CHANGED_PERSONAL_INFORMATION = "CHANGED_PERSONAL_INFORMATION"
    CHANGED_ORGANIZATION_SETTINGS = "CHANGED_ORGANIZATION_SETTINGS"
    ENABLED_INTEGRATION = "ENABLED_INTEGRATION"
    DISABLED_INTEGRATION = "DISABLED_INTEGRATION"
    ENABLED_CATEGORY = "ENABLED_CATEGORY"
    DISABLED_CATEGORY = "DISABLED_CATEGORY"
    CHANGED_PASSWORD = "CHANGED_PASSWORD"
    RESET_PASSWORD = "RESET_PASSWORD"
    ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION = "ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION"
    ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT = "ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT"
    DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION = "DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION"
    DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT = "DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT"
    CREATED_INTEGRATION_WIDE_FIELD_MAPPING = "CREATED_INTEGRATION_WIDE_FIELD_MAPPING"
    CREATED_LINKED_ACCOUNT_FIELD_MAPPING = "CREATED_LINKED_ACCOUNT_FIELD_MAPPING"
    CHANGED_INTEGRATION_WIDE_FIELD_MAPPING = "CHANGED_INTEGRATION_WIDE_FIELD_MAPPING"
    CHANGED_LINKED_ACCOUNT_FIELD_MAPPING = "CHANGED_LINKED_ACCOUNT_FIELD_MAPPING"
    DELETED_INTEGRATION_WIDE_FIELD_MAPPING = "DELETED_INTEGRATION_WIDE_FIELD_MAPPING"
    DELETED_LINKED_ACCOUNT_FIELD_MAPPING = "DELETED_LINKED_ACCOUNT_FIELD_MAPPING"
    FORCED_LINKED_ACCOUNT_RESYNC = "FORCED_LINKED_ACCOUNT_RESYNC"
    MUTED_ISSUE = "MUTED_ISSUE"
    GENERATED_MAGIC_LINK = "GENERATED_MAGIC_LINK"
    ENABLED_MERGE_WEBHOOK = "ENABLED_MERGE_WEBHOOK"
    DISABLED_MERGE_WEBHOOK = "DISABLED_MERGE_WEBHOOK"
    MERGE_WEBHOOK_TARGET_CHANGED = "MERGE_WEBHOOK_TARGET_CHANGED"
    END_USER_CREDENTIALS_ACCESSED = "END_USER_CREDENTIALS_ACCESSED"

    def visit(
        self,
        created_remote_production_api_key: typing.Callable[[], T_Result],
        deleted_remote_production_api_key: typing.Callable[[], T_Result],
        created_test_api_key: typing.Callable[[], T_Result],
        deleted_test_api_key: typing.Callable[[], T_Result],
        regenerated_production_api_key: typing.Callable[[], T_Result],
        invited_user: typing.Callable[[], T_Result],
        two_factor_auth_enabled: typing.Callable[[], T_Result],
        two_factor_auth_disabled: typing.Callable[[], T_Result],
        deleted_linked_account: typing.Callable[[], T_Result],
        created_destination: typing.Callable[[], T_Result],
        deleted_destination: typing.Callable[[], T_Result],
        changed_destination: typing.Callable[[], T_Result],
        changed_scopes: typing.Callable[[], T_Result],
        changed_personal_information: typing.Callable[[], T_Result],
        changed_organization_settings: typing.Callable[[], T_Result],
        enabled_integration: typing.Callable[[], T_Result],
        disabled_integration: typing.Callable[[], T_Result],
        enabled_category: typing.Callable[[], T_Result],
        disabled_category: typing.Callable[[], T_Result],
        changed_password: typing.Callable[[], T_Result],
        reset_password: typing.Callable[[], T_Result],
        enabled_redact_unmapped_data_for_organization: typing.Callable[[], T_Result],
        enabled_redact_unmapped_data_for_linked_account: typing.Callable[[], T_Result],
        disabled_redact_unmapped_data_for_organization: typing.Callable[[], T_Result],
        disabled_redact_unmapped_data_for_linked_account: typing.Callable[[], T_Result],
        created_integration_wide_field_mapping: typing.Callable[[], T_Result],
        created_linked_account_field_mapping: typing.Callable[[], T_Result],
        changed_integration_wide_field_mapping: typing.Callable[[], T_Result],
        changed_linked_account_field_mapping: typing.Callable[[], T_Result],
        deleted_integration_wide_field_mapping: typing.Callable[[], T_Result],
        deleted_linked_account_field_mapping: typing.Callable[[], T_Result],
        forced_linked_account_resync: typing.Callable[[], T_Result],
        muted_issue: typing.Callable[[], T_Result],
        generated_magic_link: typing.Callable[[], T_Result],
        enabled_merge_webhook: typing.Callable[[], T_Result],
        disabled_merge_webhook: typing.Callable[[], T_Result],
        merge_webhook_target_changed: typing.Callable[[], T_Result],
        end_user_credentials_accessed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventTypeEnum.CREATED_REMOTE_PRODUCTION_API_KEY:
            return created_remote_production_api_key()
        if self is EventTypeEnum.DELETED_REMOTE_PRODUCTION_API_KEY:
            return deleted_remote_production_api_key()
        if self is EventTypeEnum.CREATED_TEST_API_KEY:
            return created_test_api_key()
        if self is EventTypeEnum.DELETED_TEST_API_KEY:
            return deleted_test_api_key()
        if self is EventTypeEnum.REGENERATED_PRODUCTION_API_KEY:
            return regenerated_production_api_key()
        if self is EventTypeEnum.INVITED_USER:
            return invited_user()
        if self is EventTypeEnum.TWO_FACTOR_AUTH_ENABLED:
            return two_factor_auth_enabled()
        if self is EventTypeEnum.TWO_FACTOR_AUTH_DISABLED:
            return two_factor_auth_disabled()
        if self is EventTypeEnum.DELETED_LINKED_ACCOUNT:
            return deleted_linked_account()
        if self is EventTypeEnum.CREATED_DESTINATION:
            return created_destination()
        if self is EventTypeEnum.DELETED_DESTINATION:
            return deleted_destination()
        if self is EventTypeEnum.CHANGED_DESTINATION:
            return changed_destination()
        if self is EventTypeEnum.CHANGED_SCOPES:
            return changed_scopes()
        if self is EventTypeEnum.CHANGED_PERSONAL_INFORMATION:
            return changed_personal_information()
        if self is EventTypeEnum.CHANGED_ORGANIZATION_SETTINGS:
            return changed_organization_settings()
        if self is EventTypeEnum.ENABLED_INTEGRATION:
            return enabled_integration()
        if self is EventTypeEnum.DISABLED_INTEGRATION:
            return disabled_integration()
        if self is EventTypeEnum.ENABLED_CATEGORY:
            return enabled_category()
        if self is EventTypeEnum.DISABLED_CATEGORY:
            return disabled_category()
        if self is EventTypeEnum.CHANGED_PASSWORD:
            return changed_password()
        if self is EventTypeEnum.RESET_PASSWORD:
            return reset_password()
        if self is EventTypeEnum.ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION:
            return enabled_redact_unmapped_data_for_organization()
        if self is EventTypeEnum.ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT:
            return enabled_redact_unmapped_data_for_linked_account()
        if self is EventTypeEnum.DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION:
            return disabled_redact_unmapped_data_for_organization()
        if self is EventTypeEnum.DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT:
            return disabled_redact_unmapped_data_for_linked_account()
        if self is EventTypeEnum.CREATED_INTEGRATION_WIDE_FIELD_MAPPING:
            return created_integration_wide_field_mapping()
        if self is EventTypeEnum.CREATED_LINKED_ACCOUNT_FIELD_MAPPING:
            return created_linked_account_field_mapping()
        if self is EventTypeEnum.CHANGED_INTEGRATION_WIDE_FIELD_MAPPING:
            return changed_integration_wide_field_mapping()
        if self is EventTypeEnum.CHANGED_LINKED_ACCOUNT_FIELD_MAPPING:
            return changed_linked_account_field_mapping()
        if self is EventTypeEnum.DELETED_INTEGRATION_WIDE_FIELD_MAPPING:
            return deleted_integration_wide_field_mapping()
        if self is EventTypeEnum.DELETED_LINKED_ACCOUNT_FIELD_MAPPING:
            return deleted_linked_account_field_mapping()
        if self is EventTypeEnum.FORCED_LINKED_ACCOUNT_RESYNC:
            return forced_linked_account_resync()
        if self is EventTypeEnum.MUTED_ISSUE:
            return muted_issue()
        if self is EventTypeEnum.GENERATED_MAGIC_LINK:
            return generated_magic_link()
        if self is EventTypeEnum.ENABLED_MERGE_WEBHOOK:
            return enabled_merge_webhook()
        if self is EventTypeEnum.DISABLED_MERGE_WEBHOOK:
            return disabled_merge_webhook()
        if self is EventTypeEnum.MERGE_WEBHOOK_TARGET_CHANGED:
            return merge_webhook_target_changed()
        if self is EventTypeEnum.END_USER_CREDENTIALS_ACCESSED:
            return end_user_credentials_accessed()

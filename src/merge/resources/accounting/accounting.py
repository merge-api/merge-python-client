# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .items import Items, AsyncItems
from .issues import Issues, AsyncIssues
from .accounts import Accounts, AsyncAccounts
from .contacts import Contacts, AsyncContacts
from .expenses import Expenses, AsyncExpenses
from .invoices import Invoices, AsyncInvoices
from .payments import Payments, AsyncPayments
from .addresses import Addresses, AsyncAddresses
from .tax_rates import TaxRates, AsyncTaxRates
from ..._resource import SyncAPIResource, AsyncAPIResource
from .attachments import Attachments, AsyncAttachments
from .link_tokens import LinkTokens, AsyncLinkTokens
from .remote_keys import RemoteKeys, AsyncRemoteKeys
from .sync_status import SyncStatus, AsyncSyncStatus
from .company_info import CompanyInfoResource, AsyncCompanyInfoResource
from .credit_notes import CreditNotes, AsyncCreditNotes
from .transactions import Transactions, AsyncTransactions
from .phone_numbers import PhoneNumbers, AsyncPhoneNumbers
from .account_tokens import AccountTokens, AsyncAccountTokens
from .balance_sheets import BalanceSheets, AsyncBalanceSheets
from .selective_sync import SelectiveSync, AsyncSelectiveSync
from .vendor_credits import VendorCredits, AsyncVendorCredits
from .account_details import AccountDetails, AsyncAccountDetails
from .journal_entries import JournalEntries, AsyncJournalEntries
from .linked_accounts import LinkedAccounts, AsyncLinkedAccounts
from .purchase_orders import PurchaseOrders, AsyncPurchaseOrders
from .available_actions import AvailableActions, AsyncAvailableActions
from .income_statements import IncomeStatements, AsyncIncomeStatements
from .webhook_receivers import WebhookReceivers, AsyncWebhookReceivers
from .common_model_scopes import CommonModelScopes, AsyncCommonModelScopes
from .tracking_categories import TrackingCategories, AsyncTrackingCategories
from .cash_flow_statements import CashFlowStatements, AsyncCashFlowStatements
from .passthrough_requests import PassthroughRequests, AsyncPassthroughRequests

if TYPE_CHECKING:
    from ..._client import Merge, AsyncMerge

__all__ = ["Accounting", "AsyncAccounting"]


class Accounting(SyncAPIResource):
    accounts: Accounts
    addresses: Addresses
    attachments: Attachments
    balance_sheets: BalanceSheets
    cash_flow_statements: CashFlowStatements
    company_info: CompanyInfoResource
    contacts: Contacts
    credit_notes: CreditNotes
    expenses: Expenses
    income_statements: IncomeStatements
    invoices: Invoices
    items: Items
    journal_entries: JournalEntries
    payments: Payments
    phone_numbers: PhoneNumbers
    purchase_orders: PurchaseOrders
    tax_rates: TaxRates
    tracking_categories: TrackingCategories
    transactions: Transactions
    vendor_credits: VendorCredits
    account_details: AccountDetails
    account_tokens: AccountTokens
    link_tokens: LinkTokens
    available_actions: AvailableActions
    remote_keys: RemoteKeys
    issues: Issues
    common_model_scopes: CommonModelScopes
    passthrough_requests: PassthroughRequests
    sync_status: SyncStatus
    webhook_receivers: WebhookReceivers
    linked_accounts: LinkedAccounts
    selective_sync: SelectiveSync

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.accounts = Accounts(client)
        self.addresses = Addresses(client)
        self.attachments = Attachments(client)
        self.balance_sheets = BalanceSheets(client)
        self.cash_flow_statements = CashFlowStatements(client)
        self.company_info = CompanyInfoResource(client)
        self.contacts = Contacts(client)
        self.credit_notes = CreditNotes(client)
        self.expenses = Expenses(client)
        self.income_statements = IncomeStatements(client)
        self.invoices = Invoices(client)
        self.items = Items(client)
        self.journal_entries = JournalEntries(client)
        self.payments = Payments(client)
        self.phone_numbers = PhoneNumbers(client)
        self.purchase_orders = PurchaseOrders(client)
        self.tax_rates = TaxRates(client)
        self.tracking_categories = TrackingCategories(client)
        self.transactions = Transactions(client)
        self.vendor_credits = VendorCredits(client)
        self.account_details = AccountDetails(client)
        self.account_tokens = AccountTokens(client)
        self.link_tokens = LinkTokens(client)
        self.available_actions = AvailableActions(client)
        self.remote_keys = RemoteKeys(client)
        self.issues = Issues(client)
        self.common_model_scopes = CommonModelScopes(client)
        self.passthrough_requests = PassthroughRequests(client)
        self.sync_status = SyncStatus(client)
        self.webhook_receivers = WebhookReceivers(client)
        self.linked_accounts = LinkedAccounts(client)
        self.selective_sync = SelectiveSync(client)


class AsyncAccounting(AsyncAPIResource):
    accounts: AsyncAccounts
    addresses: AsyncAddresses
    attachments: AsyncAttachments
    balance_sheets: AsyncBalanceSheets
    cash_flow_statements: AsyncCashFlowStatements
    company_info: AsyncCompanyInfoResource
    contacts: AsyncContacts
    credit_notes: AsyncCreditNotes
    expenses: AsyncExpenses
    income_statements: AsyncIncomeStatements
    invoices: AsyncInvoices
    items: AsyncItems
    journal_entries: AsyncJournalEntries
    payments: AsyncPayments
    phone_numbers: AsyncPhoneNumbers
    purchase_orders: AsyncPurchaseOrders
    tax_rates: AsyncTaxRates
    tracking_categories: AsyncTrackingCategories
    transactions: AsyncTransactions
    vendor_credits: AsyncVendorCredits
    account_details: AsyncAccountDetails
    account_tokens: AsyncAccountTokens
    link_tokens: AsyncLinkTokens
    available_actions: AsyncAvailableActions
    remote_keys: AsyncRemoteKeys
    issues: AsyncIssues
    common_model_scopes: AsyncCommonModelScopes
    passthrough_requests: AsyncPassthroughRequests
    sync_status: AsyncSyncStatus
    webhook_receivers: AsyncWebhookReceivers
    linked_accounts: AsyncLinkedAccounts
    selective_sync: AsyncSelectiveSync

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.accounts = AsyncAccounts(client)
        self.addresses = AsyncAddresses(client)
        self.attachments = AsyncAttachments(client)
        self.balance_sheets = AsyncBalanceSheets(client)
        self.cash_flow_statements = AsyncCashFlowStatements(client)
        self.company_info = AsyncCompanyInfoResource(client)
        self.contacts = AsyncContacts(client)
        self.credit_notes = AsyncCreditNotes(client)
        self.expenses = AsyncExpenses(client)
        self.income_statements = AsyncIncomeStatements(client)
        self.invoices = AsyncInvoices(client)
        self.items = AsyncItems(client)
        self.journal_entries = AsyncJournalEntries(client)
        self.payments = AsyncPayments(client)
        self.phone_numbers = AsyncPhoneNumbers(client)
        self.purchase_orders = AsyncPurchaseOrders(client)
        self.tax_rates = AsyncTaxRates(client)
        self.tracking_categories = AsyncTrackingCategories(client)
        self.transactions = AsyncTransactions(client)
        self.vendor_credits = AsyncVendorCredits(client)
        self.account_details = AsyncAccountDetails(client)
        self.account_tokens = AsyncAccountTokens(client)
        self.link_tokens = AsyncLinkTokens(client)
        self.available_actions = AsyncAvailableActions(client)
        self.remote_keys = AsyncRemoteKeys(client)
        self.issues = AsyncIssues(client)
        self.common_model_scopes = AsyncCommonModelScopes(client)
        self.passthrough_requests = AsyncPassthroughRequests(client)
        self.sync_status = AsyncSyncStatus(client)
        self.webhook_receivers = AsyncWebhookReceivers(client)
        self.linked_accounts = AsyncLinkedAccounts(client)
        self.selective_sync = AsyncSelectiveSync(client)

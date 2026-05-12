import os
import pytest
from merge import Merge
from merge.resources.accounting.resources.contacts.types.contacts_list_request_expand import ContactsListRequestExpand
from merge.resources.accounting.resources.contacts.types.contacts_retrieve_request_expand import ContactsRetrieveRequestExpand
from merge.resources.accounting.resources.invoices.types.invoices_list_request_expand import InvoicesListRequestExpand
from merge.resources.accounting.resources.invoices.types.invoices_retrieve_request_expand import InvoicesRetrieveRequestExpand


@pytest.fixture
def client():
    account_token = os.environ["SDK_TESTING_ACCOUNTING_ACCOUNT_TOKEN"]
    api_key = os.environ["SDK_TESTING_KEY_SECONDARY"]

    return Merge(
        account_token=account_token,
        api_key=api_key,
    )


def test_account_details_retrieve(client):
    account_details = client.accounting.account_details.retrieve()
    assert account_details is not None
    assert hasattr(account_details, 'id')


def test_accounts_list(client):
    response = client.accounting.accounts.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_accounts_retrieve(client):
    accounts_response = client.accounting.accounts.list(page_size=1)

    if accounts_response.results:
        account_id = accounts_response.results[0].id
        account = client.accounting.accounts.retrieve(id=account_id)
        assert account is not None
        assert account.id == account_id


def test_attachments_list(client):
    response = client.accounting.attachments.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_attachments_retrieve(client):
    attachments_response = client.accounting.attachments.list(page_size=1)

    if attachments_response.results:
        attachment_id = attachments_response.results[0].id
        attachment = client.accounting.attachments.retrieve(id=attachment_id)
        assert attachment is not None
        assert attachment.id == attachment_id


def test_balance_sheets_list(client):
    response = client.accounting.balance_sheets.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_balance_sheets_retrieve(client):
    balance_sheets_response = client.accounting.balance_sheets.list(page_size=1)

    if balance_sheets_response.results:
        balance_sheet_id = balance_sheets_response.results[0].id
        balance_sheet = client.accounting.balance_sheets.retrieve(id=balance_sheet_id)
        assert balance_sheet is not None
        assert balance_sheet.id == balance_sheet_id


def test_vendor_credits_list(client):
    response = client.accounting.vendor_credits.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_vendor_credits_retrieve(client):
    vendor_credits_response = client.accounting.vendor_credits.list(page_size=1)

    if vendor_credits_response.results:
        vendor_credit_id = vendor_credits_response.results[0].id
        vendor_credit = client.accounting.vendor_credits.retrieve(id=vendor_credit_id)
        assert vendor_credit is not None
        assert vendor_credit.id == vendor_credit_id


def test_transactions_list(client):
    response = client.accounting.transactions.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_transactions_retrieve(client):
    transactions_response = client.accounting.transactions.list(page_size=1)

    if transactions_response.results:
        transaction_id = transactions_response.results[0].id
        transaction = client.accounting.transactions.retrieve(id=transaction_id)
        assert transaction is not None
        assert transaction.id == transaction_id


def test_tracking_categories_list(client):
    response = client.accounting.tracking_categories.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_tracking_categories_retrieve(client):
    tracking_categories_response = client.accounting.tracking_categories.list(page_size=1)

    if tracking_categories_response.results:
        tracking_category_id = tracking_categories_response.results[0].id
        tracking_category = client.accounting.tracking_categories.retrieve(id=tracking_category_id)
        assert tracking_category is not None
        assert tracking_category.id == tracking_category_id


def test_tax_rates_list(client):
    response = client.accounting.tax_rates.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_tax_rates_retrieve(client):
    tax_rates_response = client.accounting.tax_rates.list(page_size=1)

    if tax_rates_response.results:
        tax_rate_id = tax_rates_response.results[0].id
        tax_rate = client.accounting.tax_rates.retrieve(id=tax_rate_id)
        assert tax_rate is not None
        assert tax_rate.id == tax_rate_id


def test_purchase_orders_list(client):
    response = client.accounting.purchase_orders.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_purchase_orders_retrieve(client):
    purchase_orders_response = client.accounting.purchase_orders.list(page_size=1)

    if purchase_orders_response.results:
        purchase_order_id = purchase_orders_response.results[0].id
        purchase_order = client.accounting.purchase_orders.retrieve(id=purchase_order_id)
        assert purchase_order is not None
        assert purchase_order.id == purchase_order_id


def test_projects_list(client):
    response = client.accounting.projects.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_projects_retrieve(client):
    projects_response = client.accounting.projects.list(page_size=1)

    if projects_response.results:
        project_id = projects_response.results[0].id
        project = client.accounting.projects.retrieve(id=project_id)
        assert project is not None
        assert project.id == project_id


def test_payment_terms_list(client):
    response = client.accounting.payment_terms.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_payment_terms_retrieve(client):
    payment_terms_response = client.accounting.payment_terms.list(page_size=1)

    if payment_terms_response.results:
        payment_term_id = payment_terms_response.results[0].id
        payment_term = client.accounting.payment_terms.retrieve(id=payment_term_id)
        assert payment_term is not None
        assert payment_term.id == payment_term_id


def test_payment_methods_list(client):
    response = client.accounting.payment_methods.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_payment_methods_retrieve(client):
    payment_methods_response = client.accounting.payment_methods.list(page_size=1)

    if payment_methods_response.results:
        payment_method_id = payment_methods_response.results[0].id
        payment_method = client.accounting.payment_methods.retrieve(id=payment_method_id)
        assert payment_method is not None
        assert payment_method.id == payment_method_id


def test_payments_list(client):
    response = client.accounting.payments.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_payments_retrieve(client):
    payments_response = client.accounting.payments.list(page_size=1)

    if payments_response.results:
        payment_id = payments_response.results[0].id
        payment = client.accounting.payments.retrieve(id=payment_id)
        assert payment is not None
        assert payment.id == payment_id


def test_journal_entries_list(client):
    response = client.accounting.journal_entries.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_journal_entries_retrieve(client):
    journal_entries_response = client.accounting.journal_entries.list(page_size=1)

    if journal_entries_response.results:
        journal_entry_id = journal_entries_response.results[0].id
        journal_entry = client.accounting.journal_entries.retrieve(id=journal_entry_id)
        assert journal_entry is not None
        assert journal_entry.id == journal_entry_id


def test_items_list(client):
    response = client.accounting.items.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_items_retrieve(client):
    items_response = client.accounting.items.list(page_size=1)

    if items_response.results:
        item_id = items_response.results[0].id
        item = client.accounting.items.retrieve(id=item_id)
        assert item is not None
        assert item.id == item_id


def test_invoices_list(client):
    response = client.accounting.invoices.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_invoices_retrieve(client):
    invoices_response = client.accounting.invoices.list(page_size=1)

    if invoices_response.results:
        invoice_id = invoices_response.results[0].id
        invoice = client.accounting.invoices.retrieve(id=invoice_id)
        assert invoice is not None
        assert invoice.id == invoice_id


def test_income_statements_list(client):
    response = client.accounting.income_statements.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_income_statements_retrieve(client):
    income_statements_response = client.accounting.income_statements.list(page_size=1)

    if income_statements_response.results:
        income_statement_id = income_statements_response.results[0].id
        income_statement = client.accounting.income_statements.retrieve(id=income_statement_id)
        assert income_statement is not None
        assert income_statement.id == income_statement_id


def test_general_ledger_transactions_list(client):
    response = client.accounting.general_ledger_transactions.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_general_ledger_transactions_retrieve(client):
    general_ledger_transactions_response = client.accounting.general_ledger_transactions.list(page_size=1)

    if general_ledger_transactions_response.results:
        general_ledger_transaction_id = general_ledger_transactions_response.results[0].id
        general_ledger_transaction = client.accounting.general_ledger_transactions.retrieve(id=general_ledger_transaction_id)
        assert general_ledger_transaction is not None
        assert general_ledger_transaction.id == general_ledger_transaction_id


def test_expenses_list(client):
    response = client.accounting.expenses.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_expenses_retrieve(client):
    expenses_response = client.accounting.expenses.list(page_size=1)

    if expenses_response.results:
        expense_id = expenses_response.results[0].id
        expense = client.accounting.expenses.retrieve(id=expense_id)
        assert expense is not None
        assert expense.id == expense_id


def test_employees_list(client):
    response = client.accounting.employees.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_employees_retrieve(client):
    employees_response = client.accounting.employees.list(page_size=1)

    if employees_response.results:
        employee_id = employees_response.results[0].id
        employee = client.accounting.employees.retrieve(id=employee_id)
        assert employee is not None
        assert employee.id == employee_id


def test_credit_notes_list(client):
    response = client.accounting.credit_notes.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_credit_notes_retrieve(client):
    credit_notes_response = client.accounting.credit_notes.list(page_size=1)

    if credit_notes_response.results:
        credit_note_id = credit_notes_response.results[0].id
        credit_note = client.accounting.credit_notes.retrieve(id=credit_note_id)
        assert credit_note is not None
        assert credit_note.id == credit_note_id


def test_contacts_list(client):
    response = client.accounting.contacts.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_contacts_retrieve(client):
    contacts_response = client.accounting.contacts.list(page_size=1)

    if contacts_response.results:
        contact_id = contacts_response.results[0].id
        contact = client.accounting.contacts.retrieve(id=contact_id)
        assert contact is not None
        assert contact.id == contact_id


def test_company_info_list(client):
    response = client.accounting.company_info.list()
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_company_info_retrieve(client):
    company_info_response = client.accounting.company_info.list(page_size=1)

    if company_info_response.results:
        company_info_id = company_info_response.results[0].id
        company_info = client.accounting.company_info.retrieve(id=company_info_id)
        assert company_info is not None
        assert company_info.id == company_info_id


def test_contacts_list_with_expand_addresses(client):
    response = client.accounting.contacts.list(expand=ContactsListRequestExpand.ADDRESSES)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_contacts_list_with_expand_company(client):
    response = client.accounting.contacts.list(expand=ContactsListRequestExpand.COMPANY)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_contacts_retrieve_with_expand_addresses(client):
    contacts_response = client.accounting.contacts.list(page_size=1)

    if contacts_response.results:
        contact_id = contacts_response.results[0].id
        contact = client.accounting.contacts.retrieve(id=contact_id, expand=ContactsRetrieveRequestExpand.ADDRESSES)
        assert contact is not None
        assert contact.id == contact_id


def test_invoices_list_with_expand_line_items(client):
    response = client.accounting.invoices.list(expand=InvoicesListRequestExpand.LINE_ITEMS)
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_invoices_retrieve_with_expand_line_items(client):
    invoices_response = client.accounting.invoices.list(page_size=1)

    if invoices_response.results:
        invoice_id = invoices_response.results[0].id
        invoice = client.accounting.invoices.retrieve(id=invoice_id, expand=InvoicesRetrieveRequestExpand.LINE_ITEMS)
        assert invoice is not None
        assert invoice.id == invoice_id


def test_contacts_list_with_expand_string(client):
    response = client.accounting.contacts.list(expand="addresses")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)


def test_invoices_list_with_expand_string(client):
    response = client.accounting.invoices.list(expand="line_items")
    assert response is not None
    assert hasattr(response, 'results')
    assert isinstance(response.results, list)



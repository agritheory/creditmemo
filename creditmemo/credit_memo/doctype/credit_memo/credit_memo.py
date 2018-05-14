# Copyright (c) 2018, Who Agency and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.data import date_diff, today


class CreditMemo(Document):
	def validate(self):
		self.validate_cm()

	def on_submit(self):
		self.create_cm()

	def on_cancel(self):
		self.reverse_cm()

	def validate_cm(self):
		self.amount = abs(self.amount)
		# cannot exceed invoice amount
		gt = frappe.db.get_value("Sales Invoice", self.invoice, "grand_total")
		if self.amount > gt:
			frappe.throw("Credit Memo amount cannot exceed amount of Invoice. Issue multiple Credit Memos instead. \
			The total of this invoice is $" + '{:0.2f}'.format(gt) + ".", title="Validation Error")
		# cannot be before invoice date
		pd = frappe.db.get_value("Sales Invoice", self.invoice, "posting_date")
		if date_diff(self.date, pd) < 0:
			frappe.throw("Date of Credit Memo cannot be set before Sales Invoice date.  \
			Sales Invoice date is " + '{:%m-%d-%Y}'.format(pd) + ".", title="Validation Error")
		self.status = "Open"

	def create_cm(self):
		je = frappe.new_doc("Journal Entry")
		if not self.company:
			je.company = frappe.db.get_single_value("Global Defaults", "default_company")
			self.company = je.company
		else:
			je.company = self.company
		je.voucher_type = "Credit Note"
		je.posting_date = self.date
		je.cheque_date = self.date
		je.cheque_no = self.name + " from " + self.invoice
		print(je.company,  frappe.db.get_value("Company", je.company, "default_income_account"), frappe.db.get_value("Company", je.company, "default_receivable_account"))
		je.append("accounts", {
			"account": frappe.db.get_value("Company", je.company, "default_income_account"),  # Default
			"party_type": "Customer",
			"party": self.customer,
			"credit_in_account_currency": self.amount,
			"debit_in_account_currency": 0,
			"is_advance": "Yes"})
		je.append("accounts", {
			"account": frappe.db.get_value("Company", je.company, "default_receivable_account"),  # Default
			"party_type": "Customer",
			"party": self.customer,
			"credit_in_account_currency": 0,
			"debit_in_account_currency": self.amount,
			"is_advance": "No"})
		je.remark = "Credit Memo (" + self.name + ") "
		je.save()
		self.journal_entry = je.name
		je.submit()
		frappe.db.commit()

	def reverse_cm(self):
		je = frappe.new_doc("Journal Entry")
		if not self.company:
			je.company = frappe.db.get_single_value("Global Defaults", "default_company")
			self.company = je.company
		else:
			je.company = self.company
		je.voucher_type = "Credit Note"
		je.posting_date = today()
		je.cheque_date = today()
		je.cheque_no = "Cancellation of " + self.name + " from " + self.invoice
		je.append("accounts", {
			"account": frappe.db.get_value("Company", je.company, "default_receivable_account"),  # Default
			"party_type": "Customer",
			"party": self.customer,
			"credit_in_account_currency": 0,
			"debit_in_account_currency": self.amount,
			"is_advance": "No"})
		je.append("accounts", {
			"account": frappe.db.get_value("Company", je.company, "default_income_account"),  # Default
			"credit_in_account_currency": self.amount,
			"debit_in_account_currency": 0,
			"is_advance": "No"})
		je.remark = "Credit Memo (" + self.name + ") "
		je.save()
		self.journal_entry = je.name
		je.submit()
		frappe.db.commit()

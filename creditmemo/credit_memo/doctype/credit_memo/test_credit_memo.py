# -*- coding: utf-8 -*-
# Copyright (c) 2018, Who Agency and Contributors
# See license.txt

# run only this test with bench command:
# bench run-tests --doctype "Credit Memo"

from __future__ import unicode_literals

import frappe
from frappe.utils import getdate, flt
from frappe.utils.data import date_diff
import unittest
import credit_memo


class TestCreditMemo(unittest.TestCase):
    def setUp(self):
        # test_records = frappe.get_test_records("Credit Memo")
        self.test_validate_cm()

    def test_validate_cm(self):
        self.amount = flt("500.00")
        gt = flt("400.00")
        self.assertFalse(self.amount < gt)

        self.date = getdate("01-02-2018")
        pd = getdate("01-01-2018")
        self.assertTrue(date_diff(self.date, pd) < 0)

# test create_cm

# test revese_cm

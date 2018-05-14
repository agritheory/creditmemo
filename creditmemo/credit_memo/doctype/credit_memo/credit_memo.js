// Copyright (c) 2018, Who Agency and contributors
// For license information, please see license.txt

frappe.ui.form.on('Credit Memo', {
	refresh: function(frm) {
	}
});


frappe.ui.form.on("Credit Memo", "customer", function(frm) {
	cur_frm.set_query("invoice", function() {
		return {
			"filters": {
				"customer": cur_frm.doc.customer,
			}
		};
	});
});

frappe.ui.form.on("Credit Memo", "invoice", function(frm) {
	frappe.call({
		"method": "frappe.client.get_value",
		"args": {
			"doctype": "Sales Invoice",
			"filters": {"name": cur_frm.doc.invoice},
			"fieldname": "grand_total",
		},
		callback: function(r) {
			frappe.notify("Amount cannot exceed $" + r.message["grand_total"].toFixed(2)
					+ ", the total of " + cur_frm.doc.invoice + ".");
		}
	});
});

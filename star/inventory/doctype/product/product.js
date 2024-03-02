// Copyright (c) 2024, BTI UMS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product', {
	setup: function (frm) {
		console.log('tes setup');
		

	},
	refresh: function (frm) {
		console.log('tes refresh');
	},
	product_name: function (frm) {
		console.log('from product name');
		frappe.call()
	}

});

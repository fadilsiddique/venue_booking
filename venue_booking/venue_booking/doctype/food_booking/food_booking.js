// Copyright (c) 2021, TRidz and contributors
// For license information, please see license.txt

frappe.ui.form.on('Food Booking', {
	refresh: function(frm) {

	 }
});

frappe.ui.form.on("Food Required", {

	quantity: function(frm, cdt, cdn) {
	  var d = locals[cdt][cdn];
	  frappe.model.set_value(d.doctype, d.name, 'total2', (d.quantity * d.price2));
	  var total = 0;
	  frm.doc.meals_option.forEach(function(d) {
		  total += d.total2;
	  });
	  frm.set_value('total_amount', total);
  }

});


# -*- coding: utf-8 -*-
# Copyright (c) 2021, TRidz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VenueBooking(Document):
	def validate(self):
		venue_doc = frappe.get_doc('Venues',self.venue)
		self.total_amount = venue_doc.price

		if self.food_required=="Yes":
			frappe.msgprint("Remember your Venue Booking ID for food booking")

		if self.food_required=="No":
			frappe.msgprint("Thank you for booking")

		else:
			pass

		venue_doc.append('booking_status',{
			'parent_field':'booking_status',
			'booked_by': self.customer,
			'from_date': self.from_date

		})

		venue_doc.save()




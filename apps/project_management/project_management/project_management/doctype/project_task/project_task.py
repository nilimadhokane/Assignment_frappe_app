# -*- coding: utf-8 -*-
# Copyright (c) 2021, nilima and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProjectTask(Document):
	def after_insert(self):
		#frappe.sendmail(recipients='',message="task assigned!")
		frappe.sendmail(recipients='abc@gmail.com', message='task assigned!')
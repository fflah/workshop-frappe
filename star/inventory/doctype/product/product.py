# Copyright (c) 2024, BTI UMS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Product(Document):
    def autoname(self):
        self.set_product_code()
        self.name = "value"
        self.no_doc = "value"

    def before_save(self):
        pass

    def set_product_code(self):
        product_name = self.product_name.split()
        product_code = "".join([kata[0].upper() for kata in product_name])
        self.product_code = product_code


@frappe.whitelist()
def get_product_food():
    result = frappe.get_all("Product", filters={"product_category": "Food"})
    return result

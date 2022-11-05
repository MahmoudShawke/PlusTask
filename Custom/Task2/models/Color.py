from odoo import fields, api, models
from datetime import date
class Color(models.Model):
    _name = 'task2.color'
    _rec_name = 'name'
    name = fields.Char()
    unit_cost= fields.Float(string='Unit Cost')

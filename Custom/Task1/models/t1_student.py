from odoo import fields, api, models


class Student(models.Model):
    _name = 'std.inherit'
    _rec_name='student_id'
    student_id = fields.Many2one('res.partner')



from odoo import fields,api,models



class Teacher(models.Model):
    _name='task.teacher'
    _rec_name = 'teacher_id'
    teacher_id = fields.Many2one('res.partner')


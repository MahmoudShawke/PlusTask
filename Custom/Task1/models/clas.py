from odoo import fields, api, models
from datetime import date
from odoo.exceptions import ValidationError

class Classes(models.Model):
    _name = 'task.class'
    name = fields.Char(compute='calc')
    subjects = fields.Selection([
        ('Phyiscs', 'physics'),
        ('English', 'English'),
        ('Arabic', 'Arabic'),

    ])
    class_id = fields.Many2one('std.inherit', string='Student')
    teacher_id = fields.Many2one('task.teacher', string='Teacher')

    @api.model
    def create(self, vals_list):
        student = self.env['std.inherit'].search([('id','=',vals_list['class_id'])])
        teacher = self.env['task.teacher'].search([('id', '=', vals_list['teacher_id'])])

        if student.student_id.country_id==teacher.teacher_id.country_id:
            return super(Classes, self).create(vals_list)

        else:
            raise ValidationError('You Can not Create with this Teacher')

    def write(self, vals_list):
        student = self.env['std.inherit'].search([('id', '=', vals_list['class_id'])])
        teacher = self.env['task.teacher'].search([('id', '=', vals_list['teacher_id'])])

        if student.student_id.country_id == teacher.teacher_id.country_id:
            return super(Classes, self).write(vals_list)

        else:
            raise ValidationError('You Can not Update with this Teacher')


    @api.onchange('class_id')
    def _change(self):

        domain = {'teacher_id': [('teacher_id.country_id', '=', self.class_id.student_id.country_id.id)]}
        return {"domain": domain}

    @api.depends('subjects')
    def calc(self):
        for rec in self:
            if rec.subjects:
                rec.name = rec.subjects + '-' + str(date.today().year) + '-' + str(date.today().month)
            else:
                rec.name = ''

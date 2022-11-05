from odoo import fields, api, models
from datetime import date


class Wall(models.Model):
    _name = 'task2.wall'
    _rec_name = 'assigned_painter'
    assigned_painter = fields.Many2one('res.partner')
    area = fields.Float(compute='_get_area')
    length = fields.Float(string='length')
    width = fields.Float(string='width')
    total_cost = fields.Float(string='Total cost',compute='_get_total')
    color = fields.Many2one('task2.color')

    @api.depends('length','width')
    def _get_area(self):
        for rec in self:
            if rec.length and rec.width:

                rec.area = rec.length * rec.width
            else:
                rec.area = ''

    @api.depends('area')
    def _get_total(self):
        for rec in self:
            if rec.area :

                rec.total_cost = rec.color.unit_cost * rec.area
            else:
                rec.total_cost = ''

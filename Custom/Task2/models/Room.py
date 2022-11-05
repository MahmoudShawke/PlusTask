from odoo import fields, api, models
from datetime import date


class Room(models.Model):
    _name = 'task2.room'
    _rec_name = 'name'
    name = fields.Many2one('task2.house')
    Walls = fields.Many2one('task2.wall', string='Wall')
    number_of_walls = fields.Integer(string='No of wall',default='1')
    total_area = fields.Float(string='Total area of wall',compute='_get_area')
    total_cost = fields.Float(string='Total cost', compute='_get_total')

    @api.depends('name')
    def get_year_name(self):
        for rec in self:
            if rec.name:

                rec.name = str(date.today().year) + '/' + str(self.cus_id.name) + '/' + str(rec._origin.id * 10)
            else:
                rec.name = ''

    @api.depends('Walls')
    def _get_area(self):
        for rec in self:
            if rec.Walls:

                rec.total_area = rec.number_of_walls * rec.Walls.area
            else:
                rec.total_area = ''

    @api.depends('number_of_walls')
    def _get_total(self):
        for rec in self:
            if rec.number_of_walls and rec.Walls:

                rec.total_cost = rec.Walls.total_cost * rec.number_of_walls
            else:
                rec.total_cost = ''

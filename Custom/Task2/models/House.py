from odoo import fields, api, models
from datetime import date
class House(models.Model):
    _name = 'task2.house'
    _rec_name = 'name'
    cus_id = fields.Many2one('res.partner')
    Rooms = fields.Many2many('task2.room', relation='house_rooms', string='Rooms')
    name = fields.Char(compute='get_year_name')


    @api.depends('cus_id')
    def get_year_name(self):
        for rec in self:
            if rec.cus_id:

                rec.name = str(date.today().year) + '/' + str(self.cus_id.name) + '/' + str(rec._origin.id*10)
            else:
                rec.name = ''

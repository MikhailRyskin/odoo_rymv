import random

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(default=str(random.randint(1, 100)), compute="_compute_test", store=True,
                       states={'draft': [('readonly', False)]})

    _sql_constraints = [
        ('check_test_length', 'CHECK(char_length(test) < 50)', 'Длина текста должна быть меньше 50 символов!'),
    ]

    @api.depends('date_order', 'order_line')
    def _compute_test(self):
        for line in self:
            date_time = line.date_order.strftime("%d/%m/%Y %H:%M:%S")
            line.test = f'{line.amount_untaxed} - {date_time}'

# -*- coding: utf-8 -*-
# © 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    partner_id = fields.Many2one(states={})

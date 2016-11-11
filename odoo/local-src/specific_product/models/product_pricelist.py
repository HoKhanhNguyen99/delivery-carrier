# -*- coding: utf-8 -*-
# © 2016 Yannick Vaucher (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models


class ProductPriceListItem(models.Model):
    _inherit = 'product.pricelist.item'

    _order = 'sequence ASC'

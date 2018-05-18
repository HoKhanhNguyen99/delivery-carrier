# © 2015 Yannick Vaucher (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class BuildingProjectTag(models.Model):
    _name = 'building.project.tag'

    name = fields.Char('Building Project Tag')

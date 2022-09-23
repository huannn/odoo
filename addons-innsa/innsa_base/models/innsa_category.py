# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class InnsaTreeType(models.Model):
    _name = 'innsa.tree.type'

    name = fields.Char("Name", required=True)

class InnsaActivity(models.Model):
    _name = 'innsa.activity'

    name = fields.Char("Name", required=True)

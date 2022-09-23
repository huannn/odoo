# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class InnsaFarmPlanting(models.Model):
    _name = 'innsa.farm.planting'

    farm_id = fields.Many2one('innsa.farm', 'Farm')
    farm_code = fields.Char(string='Farm Code', related='farm_id.code')
    farm_name = fields.Char(string='Farm Name', related='farm_id.name')

    area_id = fields.Many2one('innsa.farm.area', 'Farm Area',
                              domain="[('farm_id', '=', farm_id)]")
    area_code = fields.Char(string='Area Code', related='area_id.code')
    area_name = fields.Char(string='Area Name', related='area_id.name')

    slot_id = fields.Many2one('innsa.farm.slot', 'Farm Slot',
                              domain="[('area_id', '=', area_id)]")
    slot_code = fields.Char(string='Slot Code', related='slot_id.code')
    slot_name = fields.Char(string='Slot Name', related='slot_id.name')

    purpose = fields.Selection([
                                ('not_used', 'Not Used'),
                                ('planting', 'In Planting'),
                                ('early_planting', 'In Early Planting')
                                ], string='Using Purpose', default='not_used')
    tree_type_id = fields.Many2one('innsa.tree.type', 'Tree Type')
    quantity = fields.Integer('Quantity')

    start_date = fields.Date('Start Date')
    manager_id = fields.Many2one('hr.employee', 'Manager')

class InnsaFarmActivity(models.Model):
    _name = 'innsa.farm.activity'

    farm_id = fields.Many2one('innsa.farm', 'Farm')
    farm_code = fields.Char(string='Farm Code', related='farm_id.code')
    farm_name = fields.Char(string='Farm Name', related='farm_id.name')

    area_id = fields.Many2one('innsa.farm.area', 'Farm Area',
                              domain="[('farm_id', '=', farm_id)]")
    area_code = fields.Char(string='Area Code', related='area_id.code')
    area_name = fields.Char(string='Area Name', related='area_id.name')

    slot_id = fields.Many2one('innsa.farm.slot', 'Farm Slot',
                              domain="[('area_id', '=', area_id)]")
    slot_code = fields.Char(string='Slot Code', related='slot_id.code')
    slot_name = fields.Char(string='Slot Name', related='slot_id.name')

    activity_id = fields.Many2one('innsa.activity', 'Activity')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    notes = fields.Text('Activity Notes')

    manager_id = fields.Many2one('hr.employee', 'Manager')

class InnsaFarmHarvest(models.Model):
    _name = 'innsa.farm.harvest'

    farm_id = fields.Many2one('innsa.farm', 'Farm')
    farm_code = fields.Char(string='Farm Code', related='farm_id.code')
    farm_name = fields.Char(string='Farm Name', related='farm_id.name')

    area_id = fields.Many2one('innsa.farm.area', 'Farm Area',
                              domain="[('farm_id', '=', farm_id)]")
    area_code = fields.Char(string='Area Code', related='area_id.code')
    area_name = fields.Char(string='Area Name', related='area_id.name')

    slot_id = fields.Many2one('innsa.farm.slot', 'Farm Slot',
                              domain="[('area_id', '=', area_id)]")
    slot_code = fields.Char(string='Slot Code', related='slot_id.code')
    slot_name = fields.Char(string='Slot Name', related='slot_id.name')

    method = fields.Selection([
        ('hai_chon', 'Hai chon'),
        ('hai_tuot', 'Hai tuot'),
        ('hai_tuot_chon', 'Hai tuot chon')
    ], string='Harvest Method')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    quantity = fields.Float('Harvest Quantity')
    harvest_code = fields.Char('Harvest Code')
    manager_id = fields.Many2one('hr.employee', 'Manager')
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class InnsaFarm(models.Model):
    _name = 'innsa.farm'

    name = fields.Char("Name", required=True)
    code = fields.Char("Code", required=True)
    address = fields.Char("Address")
    phone_number = fields.Char("Phone Number")
    google_map_link = fields.Char("Google Map Link")
    manager_id = fields.Many2one('hr.employee', 'Manager')
    map_image= fields.Image("Map Image")
    zone_ids = fields.One2many('innsa.farm.zone', 'farm_id', string='Zone Notes')
    attachment_ids = fields.Many2many('ir.attachment', string='Documents')

class InnsaFarmZone(models.Model):
    _name = 'innsa.farm.zone'

    farm_id = fields.Many2one('innsa.farm', 'Farm')
    code = fields.Char('Zone Code')
    name = fields.Char('Zone Name')
    function = fields.Char('Zone Function')

class InnsaFarmArea(models.Model):
    _name = 'innsa.farm.area'

    code = fields.Char('Area Code', required=True)
    name = fields.Char('Area Name', required=True)
    acreage = fields.Float('Acreage')
    farm_id = fields.Many2one('innsa.farm', 'Farm')
    manager_id = fields.Many2one('hr.employee', 'Manager')
    notes = fields.Text('Notes')

class InnsaFarmSlot(models.Model):
    _name = 'innsa.farm.slot'

    code = fields.Char('Slot Code', required=True)
    name = fields.Char('Slot Name', required=True)
    acreage = fields.Float('Acreage')
    farm_id = fields.Many2one('innsa.farm', 'Farm')
    area_id = fields.Many2one('innsa.farm.area', 'Farm Area',
                              domain="[('farm_id', '=', farm_id)]")
    manager_id = fields.Many2one('hr.employee', 'Manager')
    notes = fields.Text('Notes')

class InnsaFarmExperimentHistory(models.Model):
    _name = 'innsa.farm.experiment_history'

    name = fields.Char('Name', required=True)
    experiment_date = fields.Date('Experiment Date')
    experiment_organization = fields.Char('Experiment Organization')
    farm_id = fields.Many2one('innsa.farm', 'Farm')
    area_id = fields.Many2one('innsa.farm.area', 'Farm Area',
                              domain="[('farm_id', '=', farm_id)]")
    manager_id = fields.Many2one('hr.employee', 'Manager')
    notes = fields.Text('Notes')
    attachment_ids = fields.Many2many('ir.attachment', string='Documents')

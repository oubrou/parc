# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api
from odoo.modules.module import get_module_resource

class engin(models.Model):
    _name = 'hrms.engin'
    _description = 'Engin'
    
    
    @api.model
    def _default_image(self):
        image_path = get_module_resource('hrms', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())


    name= fields.Char(string="Matricule",required=True)
    type_id= fields.Many2one('hrms.engin.type',"Type engin")    
    active = fields.Boolean(default=True)
    color = fields.Integer()
    image = fields.Binary(' Pictogramme',attachment=True)
    affectation_id = fields.Many2one('hr.department',string='Affectation')
    company_id = fields.Many2one('res.company', 'Unité territorial')
    disponible = fields.Boolean("Disponible",default=True  )
    indisponible= fields.Boolean("Indisponible",default=False)
    depart_id= fields.Many2one('hrms.depart', 'N de depart')
    fonction_ids = fields.One2many(
        'hrms.engin.fonction', 'vl_id', string="Poste engin")

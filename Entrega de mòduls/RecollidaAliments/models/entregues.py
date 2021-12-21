# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class Entregues(models.Model):

    # Nom i descripció del model de dates
    _name = 'entregues'
    _description = "Model de la llista de entregues"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut organitzacio
    _rec_name="organitzacio"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    organitzacio = fields.Char("Organització") # Organització, camp format amb text
    dataHora = fields.Datetime("Data i hora") # Data i hora, camp format amb una data i hora que editarem a un calendari emergent
    pdf = fields.Binary("Fichero PDF") # PDF, camp que ens permet adjuntar un PDF amb els productes entregats
    productes = fields.Many2many('productes') # Productes, camp que contindrá tods els productes rebuts en l'entrega
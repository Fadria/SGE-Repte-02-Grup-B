# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class Voluntaris(models.Model):

    # Nom i descripció del model de dates
    _name = 'voluntaris'
    _description = "Model de la llista de voluntaris"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut nom_complet
    _rec_name="nom_complet"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    nom_complet = fields.Char("Nom Complet") # Nom complet del voluntari, camp amb text
    edat = fields.Integer("Edat") # Edat del voluntari, camp numeric
    telefon = fields.Char("Teléfon") # Telefon del voluntari, camp amb text
    email = fields.Char("Email") # Email del voluntari, camp amb text
    direccio = fields.Char("Direcció") # Direcció del voluntari, camp amb text
    zona_recollida = fields.Char("Zona de recollida") # Zona de recollida del voluntari, camp amb text
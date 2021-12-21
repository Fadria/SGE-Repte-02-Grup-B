# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class Productes(models.Model):

    # Nom i descripció del model de dates
    _name = 'productes'
    _description = "Model de la llista de productes"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut nom_producte
    _rec_name="nom_producte"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    nom_producte = fields.Char("Nom del producte") # Nom del producte, camp amb text
    data_caducitat = fields.Date("Data de caducitat") # Data de caducitat, seleccionarem la data a un calendari
    detalls = fields.Html('Detalls aliment', sanitize=True, strip_style=False) # Detalls, els omplirem a un editor de text mes avanzat
    pes = fields.Float("Pes") # Pes, camp numeric amb decimals
    ubicacio_magatzem = fields.Char("Ubicació Magatzem") # Ubicació del producte al magatzem, camp amb text
    voluntari = fields.Many2one('voluntaris') # Voluntari, relació per a indicar el voluntari que ha recollit cada producte
    entrega = fields.Many2one('entregues', 'Entrega') # Entrega, relació usada per a adjudicar un producte a una entrega

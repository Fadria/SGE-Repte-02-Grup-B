# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Productes(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'productes'

    _description = "Model de la llista de productes"

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre_completo
    _rec_name="nom_producte"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Camps del producte
    nom_producte = fields.Char("Nom del producte")
    data_caducitat = fields.Date("Data de caducitat")
    detalls = fields.Html('Detalls aliment', sanitize=True, strip_style=False)
    pes = fields.Float("Pes")
    ubicacio_magatzem = fields.Char("Ubicació Magatzem")
    voluntari = fields.Many2one('voluntaris')
    entrega = fields.Many2one('entregues', 'Entrega')
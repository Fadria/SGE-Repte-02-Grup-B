# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class llista_productes(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'llista_productes.lista'
    _description = 'Model de la llista de productes'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nom_producte"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    nom_producte = fields.Char()
    data_caducitat = fields.Date()
    detalls = fields.Html('Detalls aliment', sanitize=True, strip_style=False)
    pes = fields.Float()
    ubicacio_magatzem = fields.Char()
    voluntari = fields.Many2one('llista_voluntaris.lista')
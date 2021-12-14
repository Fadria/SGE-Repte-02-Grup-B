# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class llista_voluntaris(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'llista_voluntaris.lista'
    _description = 'Model de la llista de voluntaris'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="nom_complet"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    nom_complet = fields.Char()
    edat = fields.Integer()
    telefon = fields.Char()
    email = fields.Char()
    direccio = fields.Char()
    zona_recollida = fields.Char()
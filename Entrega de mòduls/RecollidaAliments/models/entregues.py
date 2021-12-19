# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Entregues(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'entregues'

    _description = "Model de la llista de entregues"

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre_completo
    _rec_name="organitzacio"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Camps del producte
    organitzacio = fields.Char("Organització")
    dataHora = fields.Datetime("Data i hora")
    pdf = fields.Binary("Fichero PDF")
    productes = fields.Many2many('productes')
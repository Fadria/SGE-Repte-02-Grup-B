# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Voluntaris(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'voluntaris'

    _description = "Model de la llista de voluntaris"

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre_completo
    _rec_name="nom_complet"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Campos del voluntari
    nom_complet = fields.Char("Nom Complet")
    edat = fields.Integer("Edat")
    telefon = fields.Char("Teléfon")
    email = fields.Char("Email")
    direccio = fields.Char("Direcció")
    zona_recollida = fields.Char("Zona de recollida")
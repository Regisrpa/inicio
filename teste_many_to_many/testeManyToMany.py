import os
from peewee import *

db = SqliteDatabase('animalia.db')


class Animal(Model):
    nomeDono = CharField()
    tipo_animal = CharField()
    raca = CharField()

    class Meta:
        database = db

    def __str__(self):
        return 'Tipo de animal '+ self.tipo_animal + ', Raça ' + self.raca +\
               ', Nome do dono ' + self.nomeDono

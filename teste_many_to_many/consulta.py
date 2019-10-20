import os
from peewee import *

from teste_many_to_many.testeManyToMany import Animal

db = SqliteDatabase('animalia.db')


class Consulta(Model):
    data = CharField()
    servico = CharField()
    horario = CharField()
    animal = ForeignKeyField(Animal)
    confirma = CharField()
    myID = CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.servico + 'em' + self.data + ':' + self.horario + 'comfimado+' + \
               self.confirma + ', Id da consulta: ' + self.myID + '|animal:' + str(self.animal)

if __name__ == '__main__':
    arq = 'animalia.db'
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables([Animal, Consulta])
    except OperationalError as e:
           print("erro ao criar tabelas: " + str(e))

    print("Teste do ANimal")
    a1 = Animal.create(nomeDono="jose", tipo_animal="baixo", raca="pinche")
    print(a1)

    print("TESTE DA CONSULTA")
    # criar uma consulta
    c1 = Consulta.create(data="19/09/2018", servico="Consulta de rotina",
    horario="14:00", animal=a1, confirma="N", myID="c9d8f7gu4h3hnwsik3e")
    print(c1)

    c2 = Consulta.create(data="21/09/2018", servico="Aplicação de vacina",
    horario="10:00", animal=a1, confirma="S", myID="d9firtu3434uit")

    todos = Consulta.select()
    # percorrer e mostrar as consultas
    for con in todos:
        print(con)
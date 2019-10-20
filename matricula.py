import peewee,os
db= peewee.SqliteDatabase('matricula.db')

class matricula(peewee.Model):


      class disciplina(peewee.Model):
            matematica =peewee.CharField()
            portugues=peewee.CharField()
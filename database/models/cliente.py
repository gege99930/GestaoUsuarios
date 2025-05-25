from peewee import Model, CharField, DateTimeField
from database.dataBase import db
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
import peewee

from app.v1.model.company_model import Company
from app.v1.utils.db import db


class Position(peewee.Model):
    name = peewee.CharField()
    company = peewee.ForeignKeyField(Company, backref="positions")
    salary = peewee.IntegerField()
    currency = peewee.CharField()
    link = peewee.CharField()

    class Meta:
        database = db
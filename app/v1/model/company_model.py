import peewee

from app.v1.utils.db import db


class Company(peewee.Model):
    name = peewee.CharField()
    country = peewee.CharField()

    class Meta:
        database = db
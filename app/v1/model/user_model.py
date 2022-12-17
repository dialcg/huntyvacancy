import peewee

from app.v1.utils.db import db


class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    experience_years = peewee.IntegerField()

    class Meta:
        database = db
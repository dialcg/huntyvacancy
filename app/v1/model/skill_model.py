import peewee

from app.v1.utils.db import db


class Skill(peewee.Model):
    title = peewee.CharField(unique=True, index=True)

    class Meta:
        database = db
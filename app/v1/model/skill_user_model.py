import peewee

from app.v1.utils.db import db
from .user_model import User
from .skill_model import Skill


class SkillUser(peewee.Model):
    user = peewee.ForeignKeyField(User, backref="skills")
    skill = peewee.ForeignKeyField(Skill, backref="users")
    experience_years = peewee.IntegerField()

    class Meta:
        database = db
import peewee

from app.v1.utils.db import db
from .position_model import Position
from .skill_model import Skill


class SkillPosition(peewee.Model):
    position = peewee.ForeignKeyField(Position, backref="skills")
    skill = peewee.ForeignKeyField(Skill, backref="positions")
    required_experience_years = peewee.IntegerField()

    class Meta:
        database = db
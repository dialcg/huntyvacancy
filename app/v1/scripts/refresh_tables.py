from app.v1.model.company_model import Company
from app.v1.model.position_model import Position
from app.v1.model.position_skill_model import SkillPosition
from app.v1.model.skill_model import Skill
from app.v1.model.skill_user_model import SkillUser
from app.v1.model.user_model import User
from app.v1.utils.db import db


def refresh_tables():
    with db:
        tables = [Company, Skill, User, SkillUser, Position, SkillPosition]
        db.drop_tables(tables)
        db.create_tables(tables)
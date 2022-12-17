from fastapi import HTTPException, status
from peewee import DoesNotExist
from app.v1.model.position_model import Position as PositionModel
from app.v1.model.position_skill_model import SkillPosition as SkillPositionModel
from app.v1.schema import position_schema, skill_position_schema

from .company_service import get_company_by_id
from .skill_service import get_skill_by_title


def generate_position_skills(position_skills, position_id):
    skills = []
    for skill in position_skills:
        db_skill = get_skill_by_title(skill.title)
        db_skill_position = SkillPositionModel.create(
            position=position_id,
            skill=db_skill.id,
            required_experience_years=skill.required_experience_years
        )
        db_skill_position.save()

        skills.append(skill_position_schema.SkillPosition(
            title=db_skill_position.skill.title,
            required_experience_years=db_skill_position.required_experience_years
        ))
    return skills


def get_positions():
    return [position for position in PositionModel.select()]


def get_position_by_id(id):
    return PositionModel.filter(PositionModel.id == id)


def create_position(position: position_schema.PositionRegister):
    db_position = PositionModel.filter(PositionModel.name == position.name)
    db_company = get_company_by_id(position.company)

    if db_position:
        msg = "Position already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    if not db_company:
        msg = "Position already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_position = PositionModel(
        name=position.name,
        company=position.company,
        salary=position.salary,
        currency=position.currency,
        link=position.link
    )

    db_position.save()
    
    skills_positions = generate_position_skills(position.skills, db_position.id)

    return position_schema.Position(
        id=db_position.id,
        name=db_position.name,
        company=db_position.company.id,
        salary=db_position.salary,
        currency=db_position.currency,
        link=db_position.link,
        skills=skills_positions
    )


def update_position(position: position_schema.Position):
    try:
        db_position = PositionModel.get_by_id(position.id)
    except DoesNotExist:
        msg = "Position not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
        
    db_position.name = position.name
    db_position.country = position.country

    db_position.save()

    return position_schema.Position(
        id=db_position.id,
        name=db_position.name,
        country=db_position.country
    )


def remove_position(id):
    try:
        db_position = PositionModel.get_by_id(id)
    except DoesNotExist:
        msg = "Position not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    PositionModel.delete_by_id(id)

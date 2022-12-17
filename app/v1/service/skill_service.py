from fastapi import HTTPException, status
from peewee import DoesNotExist
from app.v1.model.skill_model import Skill as SkillModel
from app.v1.schema import skill_schema


def get_skills():
    return [skill for skill in SkillModel.select()]


def get_skill_by_id(id):
    return SkillModel.filter(SkillModel.id == id)


def create_skill(skill: skill_schema.SkillRegister):
    db_skill = SkillModel.filter(SkillModel.title == skill.title)

    if db_skill:
        msg = "Skill already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_skill = SkillModel(
        title=skill.title
    )

    db_skill.save()

    return skill_schema.Skill(
        id=db_skill.id,
        title=db_skill.title
    )


def update_skill(skill: skill_schema.Skill):
    try:
        db_skill = SkillModel.get_by_id(skill.id)
    except DoesNotExist:
        msg = "Skill not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
        
    db_skill.title = skill.title

    db_skill.save()

    return skill_schema.Skill(
        id=db_skill.id,
        title=db_skill.title
    )


def get_skill_by_id(id):
    try:
        db_skill = SkillModel.get_by_id(id)
    except DoesNotExist:
        msg = "Skill not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    return skill_schema.Company(
        id=db_skill.id,
        title=db_skill.title
    )


def get_skill_by_title(title):
    try:
        db_skill = SkillModel.get(title=title)
    except DoesNotExist:
        msg = "Skill not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    return skill_schema.Skill(
        id=db_skill.id,
        title=db_skill.title
    )


def remove_skill(id):
    try:
        SkillModel.get_by_id(id)
    except DoesNotExist:
        msg = "Skill not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    SkillModel.delete_by_id(id)

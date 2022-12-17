from typing import List
from pydantic import BaseModel
from pydantic import Field
from .skill_position_schema import SkillPosition


class PositionBase(BaseModel):
    name: str = Field(...)
    company: int = Field(...)
    salary: int = Field(...)
    currency: str = Field(...)
    link: str = Field(...)
    skills: List[SkillPosition]


class Position(PositionBase):
    id: int = Field(...)

    class Config:
        orm_mode = True


class PositionRegister(PositionBase):
    pass
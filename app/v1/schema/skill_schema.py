from pydantic import BaseModel
from pydantic import Field


class SkillBase(BaseModel):
    title: str = Field(...)


class Skill(SkillBase):
    id: int = Field(...)

    class Config:
        orm_mode = True


class SkillRegister(SkillBase):
    pass
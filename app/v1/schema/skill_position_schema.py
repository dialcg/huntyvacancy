from pydantic import BaseModel
from pydantic import Field


class SkillPosition(BaseModel):
    title: str = Field(...)
    required_experience_years: int = Field(...)

    class Config:
        orm_mode = True

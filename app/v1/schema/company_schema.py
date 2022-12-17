from pydantic import BaseModel
from pydantic import Field


class CompanyBase(BaseModel):
    name: str = Field(...)
    country: str = Field(...)


class Company(CompanyBase):
    id: int = Field(...)

    class Config:
        orm_mode = True


class CompanyRegister(CompanyBase):
    pass
from fastapi import HTTPException, status
from peewee import DoesNotExist
from app.v1.model.company_model import Company as CompanyModel
from app.v1.schema import company_schema


def get_companies():
    return [company for company in CompanyModel.select()]


def get_company_by_id(id):
    try:
        db_company = CompanyModel.get_by_id(id)
    except DoesNotExist:
        msg = "Company not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    return company_schema.Company(
        id=db_company.id,
        name=db_company.name,
        country=db_company.country
    )


def create_company(company: company_schema.CompanyRegister):
    db_company = CompanyModel.filter(CompanyModel.name == company.name)

    if db_company:
        msg = "Company already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_company = CompanyModel(
        name=company.name,
        country=company.country
    )

    db_company.save()

    return company_schema.Company(
        id=db_company.id,
        name=db_company.name,
        country=db_company.country
    )


def update_company(company: company_schema.Company):
    try:
        db_company = CompanyModel.get_by_id(company.id)
    except DoesNotExist:
        msg = "Company not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
        
    db_company.name = company.name
    db_company.country = company.country

    db_company.save()

    return company_schema.Company(
        id=db_company.id,
        name=db_company.name,
        country=db_company.country
    )


def remove_company(id):
    try:
        db_company = CompanyModel.get_by_id(id)
    except DoesNotExist:
        msg = "Company not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    CompanyModel.delete_by_id(id)

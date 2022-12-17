from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from typing import List

from app.v1.schema import company_schema
from app.v1.service import company_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")


@router.get(
    "/companies/",
    tags=["companies"],
    status_code=status.HTTP_200_OK,
    response_model=List[company_schema.Company],
    dependencies=[Depends(get_db)],
    summary="Gets all companies"
)
def get_companies():
    """
    ## Get all companies in the app

    ### Args
    No args

    ### Returns
    A list of companies
    """
    return company_service.get_companies()


@router.post(
    "/companies/",
    tags=["companies"],
    status_code=status.HTTP_201_CREATED,
    response_model=company_schema.Company,
    dependencies=[Depends(get_db)],
    summary="Creates a new company"
)
def create_company(company: company_schema.CompanyRegister = Body(...)):
    """
    ## Creates a new company in the app

    ### Args
    The app can recive next fields into a JSON
    - name 
    - country

    ### Returns
    - company: DB Company info
    """

    return company_service.create_company(company)


@router.put(
    "/companies/",
    tags=["companies"],
    status_code=status.HTTP_200_OK,
    response_model=company_schema.Company,
    dependencies=[Depends(get_db)],
    summary="Updates a new company"
)
def update_company(company: company_schema.Company = Body(...)):
    """
    ## Updates a new company in the app

    ### Args
    The app can recive next fields into a JSON
    - id
    - name 
    - country

    ### Returns
    - company: DB Company info
    """

    return company_service.update_company(company)


@router.get(
    "/companies/{id}",
    tags=["companies"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Gets a single company"
)
def get_company(id: int):
    """
    ## Gets a company

    ### Args
    The app can recive next fields into a JSON
    - id
    ### Returns
    - company: DB Company info
    """

    return company_service.get_company_by_id(id)


@router.delete(
    "/companies/{id}",
    tags=["companies"],
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)],
    summary="Updates a new company"
)
def remove_company(id: int):
    """
    ## Deletes a new company in the app

    ### Args
    The app can recive next fields into a JSON
    - id
    ### Returns
    - HTTP 204
    """

    return company_service.remove_company(id)



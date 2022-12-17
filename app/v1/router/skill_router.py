from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from typing import List

from app.v1.schema import skill_schema
from app.v1.service import skill_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")


@router.get(
    "/skills/",
    tags=["skills"],
    status_code=status.HTTP_200_OK,
    response_model=List[skill_schema.Skill],
    dependencies=[Depends(get_db)],
    summary="Gets all skills"
)
def get_skills():
    """
    ## Get all skills in the app

    ### Args
    No args

    ### Returns
    A list of skills
    """
    return skill_service.get_skills()


@router.post(
    "/skills/",
    tags=["skills"],
    status_code=status.HTTP_201_CREATED,
    response_model=skill_schema.Skill,
    dependencies=[Depends(get_db)],
    summary="Creates a new skill"
)
def create_skill(skill: skill_schema.SkillRegister = Body(...)):
    """
    ## Creates a new skill in the app

    ### Args
    The app can recive next fields into a JSON
    - title 

    ### Returns
    - skill: DB Skill info
    """

    return skill_service.create_skill(skill)


@router.put(
    "/skills/",
    tags=["skills"],
    status_code=status.HTTP_200_OK,
    response_model=skill_schema.Skill,
    dependencies=[Depends(get_db)],
    summary="Updates a new skill"
)
def update_skill(skill: skill_schema.Skill = Body(...)):
    """
    ## Updates a new skill in the app

    ### Args
    The app can recive next fields into a JSON
    - id
    - title 

    ### Returns
    - skill: DB Skill info
    """

    return skill_service.update_skill(skill)


@router.delete(
    "/skills/{id}",
    tags=["skills"],
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)],
    summary="Updates a new skill"
)
def remove_skill(id: int):
    """
    ## Deletes a new skill in the app

    ### Args
    The app can recive next fields into a JSON
    - id
    ### Returns
    - HTTP 204
    """

    return skill_service.remove_skill(id)



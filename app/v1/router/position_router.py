from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from typing import List

from app.v1.schema import position_schema
from app.v1.service import position_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")


@router.get(
    "/positions/",
    tags=["positions"],
    status_code=status.HTTP_200_OK,
    response_model=List[position_schema.Position],
    dependencies=[Depends(get_db)],
    summary="Gets all positions"
)
def get_positions():
    """
    ## Get all positions in the app

    ### Args
    No args

    ### Returns
    A list of positions
    """
    return position_service.get_positions()


@router.post(
    "/positions/",
    tags=["positions"],
    status_code=status.HTTP_201_CREATED,
    response_model=position_schema.Position,
    dependencies=[Depends(get_db)],
    summary="Creates a new position"
)
def create_position(position: position_schema.PositionRegister = Body(...)):
    """
    ## Creates a new position in the app

    ### Args
    The app can recive next fields into a JSON
    - name 

    ### Returns
    - position: DB Position info
    """

    return position_service.create_position(position)


@router.put(
    "/positions/",
    tags=["positions"],
    status_code=status.HTTP_200_OK,
    response_model=position_schema.Position,
    dependencies=[Depends(get_db)],
    summary="Updates a new position"
)
def update_position(position: position_schema.Position = Body(...)):
    """
    ## Updates a new position in the app

    ### Args
    The app can recive next fields into a JSON
    - id
    - name 

    ### Returns
    - position: DB Position info
    """

    return position_service.update_position(position)


@router.delete(
    "/positions/{id}",
    tags=["positions"],
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)],
    summary="Updates a new position"
)
def remove_position(id: int):
    """
    ## Deletes a new position in the app

    ### Args
    The app can recive next fields into a JSON
    - id
    ### Returns
    - HTTP 204
    """

    return position_service.remove_position(id)



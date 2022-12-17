from fastapi import FastAPI
from app.v1.router.company_router import router as company_router
from app.v1.router.skill_router import router as skill_router
from app.v1.router.position_router import router as position_router


app = FastAPI()

app.include_router(company_router)
app.include_router(skill_router)
app.include_router(position_router)
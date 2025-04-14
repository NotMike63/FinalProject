from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['promotions'],
    prefix="/promotions"
)


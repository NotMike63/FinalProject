from fastapi import APIRouter, Depends, HTTPException
from httpx import request
from sqlalchemy.orm import Session
from ..controllers import resource_managements as controller
from ..schemas import resource_managements as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['ResourceManagements'],
    prefix="/resource_managements"
)

@router.post("/")
def create_resource_management(request: schema.ResourceManagementCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.ResourceManagement])
def read_all_resource_managements(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{resource_management_id}")
def read_one_resource_management(resource_management_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, resource_management_id=resource_management_id)

@router.put("/{resource_management_id}")
def update_one_resource_management(resource_management_id: int, request: schema.ResourceManagementUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, resource_management_id=resource_management_id, request=request)

@router.delete("/{resource_management_id}")
def delete_one_resource_management(resource_management_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, resource_management_id=resource_management_id)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/cadastrar", status_code=201)
def create_client(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return services.create_cliente(db=db, cliente=cliente)

@router.get("/listar")
def listar_clientes(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getCliente_paginate(db=db, page=page, per_page=per_page)
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/clientes", tags=["Rotas de Clientes"])

@router.post("/cadastrar", status_code=201)
def create_client(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return services.create_cliente(db=db, cliente=cliente)

@router.get("/listar")
def listar_clientes(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getCliente_paginate(db=db, page=page, per_page=per_page)

@router.delete("/deletar/{codcliente}")
def deletar_cliente(codcliente: int, db: Session = Depends(get_db)):
    
    sucesso = services.delete_cliente(db=db, cliente_id=codcliente)

    return sucesso

@router.put("/update/{codcliente}")
def update_client(codcliente: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    cliente_atualizado = services.update_cliente(db=db, cliente_id=codcliente, cliente_dados=cliente)
    
    return cliente_atualizado
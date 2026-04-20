from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/fornecedor", tags=["Rotas de Fornecedores"])

@router.post("/cadastrar", summary="Cadastrar um novo fornecedor", description="Rota para cadastrar um novo fornecedor")
def create_fornec(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    return services.create_fornecedor(db=db, fornecedor=fornecedor)

@router.delete("/excluir/{codfornec}", summary="Excluir um fornecedor", description="Rota para excluir um fornecedor")
def delete_fornec(codfornec: int, db: Session = Depends(get_db)):
    return services.excluir_fornecedor(db=db, codfornec=codfornec)

@router.get("/listar", summary="Listar todos os fornecedores", description="Rota para listar todos os fornecedores")
def list_fornec(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.list_fornecedor(db=db, page=page, per_page=per_page)

@router.put("/atualizar/{codfornec}", summary="Atualizar um fornecedor", description="Rota para atualizar os dados de um fornecedor")
def update_fornec(codfornec: int, fornecedor: schemas.FornecedorUpdate, db: Session = Depends(get_db)):
    return services.update_fornecedor(db=db, codfornec=codfornec, fornecedor_update=fornecedor)

@router.get("/listar", summary="Listar empregados com paginação", description="Rota para listar empregados com paginação")
def list_employee(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getEmployee_paginate(db=db, page=page, per_page=per_page)
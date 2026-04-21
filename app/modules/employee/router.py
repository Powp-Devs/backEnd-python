from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/empregados", tags=["Rotas para os empregados"])

@router.get("/", summary="Listar empregados com paginação")
def listar_empregados(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    return services.getEmployee_paginate(db=db, page=page, per_page=page_size)

@router.get("/{codempregado}", summary="Obter um empregado específico")
def obter_empregado(codempregado: int, db: Session = Depends(get_db)):
    return services.get_employee_by_id(db=db, codempregado=codempregado)

@router.post("/cadastrar", summary="Rota para cadastrar um novo empregado", description="Rota que permite o usuário realize o cadastro de um novo empregado no sistema")
def cadastro_employee(dados_empregado: schemas.EmpregadoCreate, db: Session = Depends(get_db)):
    return services.create_employee(db=db, dados=dados_empregado)

@router.put("/{codempregado}", summary="Rota para atualizar o empregado", description="Rota solicita dados para realizaer a atualização cadastral de um funcionário")
def atualizar_funcionario(codempregado: int, dados: schemas.EmpregadoCreate, db: Session = Depends(get_db)):
    return services.update_employee(db=db, codempregado=codempregado, dados=dados)

@router.delete("/{codempregado}", summary="Deletar um empregado")
def delete(codempregado: int, db: Session = Depends(get_db)):
    return services.delete_employee(db=db, codempregado=codempregado)
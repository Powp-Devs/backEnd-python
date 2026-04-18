from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/setor", tags=["Rotas para os setores da empresa"])

@router.get("/listar", summary="Rota para listar setores da empresa paginados", description="Rota que traz a paginação de todos os setores cadastrados na empresa")
def listar_setor_paginate(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getSector_paginate(db=db, page=page, per_page=per_page)

@router.post("/cadastrar", summary="Rota para cadastrar um novo setor da empresa", description="tyeste")
def cadastrar_setor(dados_setor: schemas.SetorCreate, db: Session = Depends(get_db)):
    return services.create_sector(db=db, dados=dados_setor)

@router.put("/inativar/{codsetor}", summary="Rota para inativar um setor")
def inativar_setor(codsetor: int, db: Session = Depends(get_db)):
    return services.inativar_sector(db=db, codsetor=codsetor)

@router.delete("delete/{codsetor}", summary="Rota para apagar o setor da empresa", description="Nessa rota é possível excluir um setor cadastrado na empresa, porém não é possível excluir um setor que tenha funcionário amarrado nele")
def delete_sec(codsetor: int, db: Session = Depends(get_db)):
    return services.delete_sector(db=db, codsetor=codsetor)
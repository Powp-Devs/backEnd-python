from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/setor", tags=["Rotas para os setores da empresa"])

@router.post("/cadastrar", summary="Rota para cadastrar um novo setor da empresa")
def cadastrar_setor(dados_setor: schemas.SetorCreate, db: Session = Depends(get_db)):
    return services.create_sector(db=db, dados=dados_setor)
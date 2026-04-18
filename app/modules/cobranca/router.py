from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/plano", tags=["Rotas para os planos e cobranças da empresa"])

@router.post("/cadastrar", summary="Rota para cadastrar um novo plano da empresa", description="Rota redará uma função que cadastra novos planos de pagamento dentro da empresa")
def cadastrar_setor(dados_setor: schemas.PlanoCreate, db: Session = Depends(get_db)):
    return services.create_plano(db=db, dados=dados_setor)
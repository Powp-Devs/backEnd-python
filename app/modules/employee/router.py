from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/empregados", tags=["Rotas para os empregados"])

@router.post("/cadastrar", summary="Rota para cadastrar um novo empregado", description="Rota que permite o usuário realize o cadastro de um novo empregado no sistema")
def cadastro_employee(dados_empregado: schemas.EmpregadoCreate, db: Session = Depends(get_db)):
    return services.create_empregrado(db=db, dados=dados_empregado)
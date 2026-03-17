from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/fornecedor", tags=["Rotas de Fornecedores"])

@router.post("/cadastrar")
def create_fornec(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    return services.create_fornecedor(db=db, fornecedor=fornecedor)
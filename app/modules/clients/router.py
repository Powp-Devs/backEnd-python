from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", status_code=201)
def create_client(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return services.create_cliente(db=db, cliente=cliente)
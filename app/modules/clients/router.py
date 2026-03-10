from fastapi import APIRouter
from .schemas import ClienteCreate
from .services import create_cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", status_code=201)
def cadastrar_cliente(cliente: ClienteCreate):
    return create_cliente(cliente)
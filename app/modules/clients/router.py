from fastapi import APIRouter
from .schemas import ClienteCreate

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", status_code=201)
def create_cliente(cliente: ClienteCreate):
    return {"message": f"Cliente {cliente.cliente} recebido com sucesso!"}
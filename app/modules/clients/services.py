from sqlalchemy.orm import Session
from . import schemas, models
from .schemas import ClienteCreate

def create_cliente(db: Session, cliente: schemas.ClienteCreate):

    new_endereco = models.
    
    new_client = models.Cliente(
        cliente = cliente.cliente,
        fantasia = cliente.fantasia,
        dtcadastro = cliente.dtcadastro,
        tipopessoa = cliente.tipopessoa,
        email = cliente.email,
        codtelefone = cliente.codtelefone,
        codendereco = cliente.codendereco,
        obs = cliente.obs,
        bloqueio = cliente.bloqueio,
        motivo_bloq = cliente.motivo_bloq
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client

def getCliente_paginate(page: int = 1, per_page: int = 10):
    total_simulado = 50
    clientes_simulados = [
        {"codcliente": 1, "cliente": "Empresa A", "email": "contato@empresaa.com"},
        {"codcliente": 2, "cliente": "Empresa B", "email": "contato@empresab.com"}
    ]

    return {
        "data": clientes_simulados,
        "total": total_simulado,
        "page": page,
        "per_page": per_page
    }
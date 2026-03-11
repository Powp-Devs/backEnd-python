from .schemas import ClienteCreate

def create_cliente(data: ClienteCreate):
    nome_cliente = data.cliente
    email_cliente = data.email

    cliente_teste = {
        "codcliente": 12,
        "cliente": nome_cliente,
        "email": email_cliente,
        "mensagem": "Cliente processado pela camada de service!"
    }

    return cliente_teste

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
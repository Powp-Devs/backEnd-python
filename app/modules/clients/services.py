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
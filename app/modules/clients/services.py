from sqlalchemy.orm import Session
from datetime import date
from fastapi import HTTPException

from .schemas import ClienteCreate
from app.modules.util import schemas, models as model_endereco
from . import schemas, models

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    try:
        new_endereco = model_endereco.Endereco(
            logradouro = cliente.logradouro,
            numero = cliente.numero,
            cep = cliente.cep,
            bairro = cliente.bairro,
            cidade = cliente.cidade,
            uf = cliente.uf,
            pais = cliente.pais   
        )
        
        new_contato = model_endereco.Contato(
            telefone = cliente.telefone,
            celular = cliente.celular,
            email = cliente.email,
            email2 = cliente.email2
        )
        
        db.add(new_endereco)
        db.add(new_contato)
        db.flush()
        
        new_client = models.Cliente(
            cliente = cliente.cliente,
            fantasia = cliente.fantasia,
            dtcadastro = cliente.dtcadastro,
            tipopessoa = cliente.tipopessoa,
            codtelefone = new_contato.codcontato, 
            codendereco = new_endereco.codendereco,
            obs = cliente.obs,
            bloqueio = cliente.bloqueio,
            motivo_bloq = cliente.motivo_bloq
        )
        
        db.add(new_client)
        db.flush()
        
        if cliente.tipopessoa == 'F':
            new_cliente_fisico = models.ClienteFisico(
                codcli = new_client.codcliente,
                cpf = cliente.cpf,
                rg = cliente.rg,
                dt_nascimento = cliente.dt_nascimento
            )
            db.add(new_cliente_fisico)
        elif cliente.tipopessoa == 'J':
            new_cliente_juridico = models.ClienteJuridico(
                codcli = new_client.codcliente,
                cnpj = cliente.cnpj,
                ie = cliente.inscricaoestadual,
                dtabertura = cliente.dtabertura
            )
            db.add(new_cliente_juridico)

        
        db.commit()
        db.refresh(new_client)

        return new_client
    except Exception as e:
        db.rollback()
        raise e #HTTPException(status_code=500, detail=str(e))

def getCliente_paginate(db: Session, page: int = 1, per_page: int = 10):
    
    offset = (page - 1) * per_page
    total_clientes = db.query(models.Cliente).count()
    
    clientes_db = db.query(models.Cliente).offset(offset).limit(per_page).all()

    return {
        "data": clientes_db,
        "total": total_clientes,
        "page": page,
        "per_page": per_page
    }
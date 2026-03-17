from sqlalchemy.orm import Session
#from datetime import date
#from fastapi import HTTPException

#from .schemas import ClienteCreate
from app.modules.util import schemas, models as model_util
from . import schemas, models

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    try:
        new_endereco = model_util.Endereco(
            logradouro = cliente.logradouro,
            numero = cliente.numero,
            cep = cliente.cep,
            bairro = cliente.bairro,
            cidade = cliente.cidade,
            uf = cliente.uf,
            pais = cliente.pais   
        )
        
        new_contato = model_util.Contato(
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
    endereco_db = db.query(model_util.Endereco).all()
    contato_db = db.query(model_util.Contato).all()

    return {
        "cliente": clientes_db, 
        "endereco": endereco_db,
        "contato": contato_db,
        "total": total_clientes,
        "page": page,
        "per_page": per_page
    }

def update_cliente(db: Session, cliente_id: int, cliente_dados: schemas.ClienteCreate):
    
    cliente_db = db.query(models.Cliente).filter(models.Cliente.codcliente == cliente_id).first()
    
    if not cliente_db:
        return {
            "code": 404,
            "message": "Cliente não encontrado",
            "success": False
        }
    
    try:
        cliente_db.cliente = cliente_dados.cliente
        cliente_db.fantasia = cliente_dados.fantasia
        cliente_db.obs = cliente_dados.obs
        cliente_db.bloqueio = cliente_dados.bloqueio
        cliente_db.motivo_bloq = cliente_dados.motivo_bloq
        
        if cliente_db.codendereco:
            endereco_db = db.query(model_util.Endereco).filter(model_util.Endereco.codendereco == cliente_db.codendereco).first()
            if endereco_db:
                endereco_db.logradouro = cliente_dados.logradouro
                endereco_db.numero = cliente_dados.numero
                endereco_db.cep = cliente_dados.cep
                endereco_db.bairro = cliente_dados.bairro
                endereco_db.cidade = cliente_dados.cidade
                endereco_db.uf = cliente_dados.uf
                endereco_db.pais = cliente_dados.pais
        else:
            return {
                "code": 404,
                "message": "Endereço não encontrado",
                "success": False
            }
        
        if cliente_db.codtelefone:
            contato_db = db.query(model_util.Contato).filter(model_util.Contato.codcontato == cliente_db.codtelefone).first()
            if contato_db:
                contato_db.telefone = cliente_dados.telefone
                contato_db.celular = cliente_dados.celular
                contato_db.email = cliente_dados.email
                if hasattr(cliente_dados, 'email2'):
                    contato_db.email2 = cliente_dados.email2
        else: 
            return {
                "code": 404,
                "message": "Contato não encontrado",
                "success": False
            }
        
        if cliente_db.tipopessoa == 'F':
            fisico_db = db.query(models.ClienteFisico).filter(models.ClienteFisico.codcli == cliente_id).first()
            if fisico_db:
                fisico_db.cpf = cliente_dados.cpf
                fisico_db.rg = cliente_dados.rg
                fisico_db.dt_nascimento = cliente_dados.dt_nascimento
        
        elif cliente_db.tipopessoa == 'J':
            juridico_db = db.query(models.ClienteJuridico).filter(models.ClienteJuridico.codcli == cliente_id).fisrt()
            if juridico_db:
                juridico_db.cnpj = cliente_dados.cnpj
                juridico_db.ie = cliente_dados.inscricaoestadual
                if hasattr(cliente_dados, 'dtabertura'):
                    juridico_db.dtabertura = cliente_dados.dtabertura
                    
        db.commit()
        db.refresh(cliente_db)
        
        return {
            "code": 200,
            "message":  "Cliente alterado com sucesso",
            "success": True,
            "data": cliente_db
        }
        
    except Exception as e:
        db.rollback()
        raise e

def delete_cliente(db: Session, cliente_id: int):
    
    cliente_db = db.query(models.Cliente).filter(models.Cliente.codcliente == cliente_id).first()
    
    if not cliente_db:
        return {
            "code": 404,
            "message": "Cliente não encontrado",
            "success": False
        }
    
    id_endereco = cliente_db.codendereco
    id_telefone = cliente_db.codtelefone
    
    if cliente_db.tipopessoa == 'F':
        db.query(models.ClienteFisico).filter(models.ClienteFisico.codcli == cliente_id).delete()
    elif cliente_db.tipopessoa == 'J':
        db.query(models.ClienteJuridico).filter(models.ClienteJuridico.codcli == cliente_id).delete()  
        
    db.delete(cliente_db)
    
    db.flush()
    
    if id_endereco:
        db.query(model_util.Endereco).filter(model_util.Endereco.codendereco == id_endereco).delete()
    if id_telefone:
        db.query(model_util.Contato).filter(model_util.Contato.codcontato == id_telefone).delete()
    
    db.commit()
    
    return {
        "code": 200,
        "message": "Cliente deletado com sucesso",
        "success": True
    }
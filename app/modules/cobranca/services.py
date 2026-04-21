from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

from . import schemas, models

def create_plano(db: Session, dados: schemas.PlanoCreate):
    try:
        new_plano = models.Plano (
            plano = dados.plano,
            numdias = dados.numdias,
            prazo1 = dados.prazo1,
            prazo2 = dados.prazo2,
            prazo3 = dados.prazo3,
            prazo4 = dados.prazo4,
            prazo5 = dados.prazo5,
            prazo6 = dados.prazo6
        )

        db.add(new_plano)
        db.flush()

        db.commit()
        db.refresh(new_plano)

        return {
            "status": 201,
            "message": "Plano de pagamento cadastrado com sucesso",
            "plano": new_plano
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível cadastrar um novo plano de pagamento. ERRO => {str(e)}")
    
def create_cobranca(db: Session, dados: schemas.CobrancaCreate):
    try:
        new_cobranca = models.Cobranca(
            cobranca = dados.cobranca,
            status = dados.status,
            dtcadastro = datetime.now()
        )

        db.add(new_cobranca)
        db.flush()

        db.commit()
        db.refresh(new_cobranca)

        return {
            "status": 201,
            "message": "Cobrança cadastrada com sucesso",
            "data": new_cobranca
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível cadastrar uma nova cobrança. ERRO => {str(e)}") 

def getPlano_paginate(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    total_planos = db.query(models.Plano).count()

    planos_db = db.query(models.Plano).offset(offset).limit(per_page).all()

    return {
        "status": 200, 
        "message": "Listagem de planos de pagamento cadastrados",
        "plano": planos_db,
        "total": total_planos,
        "page": page,
        "per_page": per_page
    }

def getCobranca_paginate(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    total_cobranca = db.query(models.Cobranca).count()

    cobranca_db = db.query(models.Cobranca).offset(offset).limit(per_page).all()

    return {
        "status": 200, 
        "message": "Listagem de planos de pagamento cadastrados",
        "plano": cobranca_db,
        "total": total_cobranca,
        "page": page,
        "per_page": per_page
    }

def inativar_plano(db: Session, codplano: int):
    plano_db = db.query(models.Plano).filter(models.Plano.codplano == codplano).first()

    if not plano_db:
        return {
            "status": 404,
            "message": "Plano não encontrado",
            "success": False
        }
    
    try: 
        plano_db.status = 'I'
        db.commit()
        db.refresh(plano_db)

        return {
            "status": 200,
            "message": "Plano de pagamento inativado com sucesso",
            "data": plano_db
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível inativar o plano de pagamento. ERRO => {str(e)}")
    
def inativar_cobranca(db: Session, codcobranca: int):
    cobranca_db = db.query(models.Cobranca).filter(models.Cobranca.codcobranca == codcobranca).first()

    if not cobranca_db:
        return {
            "status": 404,
            "message": "Cobrança não encontrada",
            "success": False
        }
    
    try: 
        cobranca_db.status = 'I'
        db.commit()
        db.refresh(cobranca_db)

        return {
            "status": 200,
            "message": "Cobrança inativada com sucesso",
            "data": cobranca_db
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível inativar a cobrança. ERRO => {str(e)}")
    
def update_plano(db: Session, codplano: int, dados: schemas.PlanoCreate):
    plano_db = db.query(models.Plano).filter(models.Plano.codplano == codplano).first()

    if not plano_db:
        return {
            "status": 404,
            "message": "Plano de pagamento não localizado",
            "success": False
        }
    
    try:
        plano_db.plano = dados.plano,
        plano_db.status = dados.status,
        plano_db.numdias = dados.numdias,
        plano_db.prazo1 = dados.prazo1,
        plano_db.prazo2 = dados.prazo2,
        plano_db.prazo3 = dados.prazo3,
        plano_db.prazo4 = dados.prazo4,
        plano_db.prazo5 = dados.prazo5,
        plano_db.prazo6 = dados.prazo6

        db.commit()
        db.refresh(plano_db)

        return {
            "status": 200,
            "message": "Plano de pagamento atualizado com sucesso",
            "success": True,
            "data": plano_db
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível atualizar o cadastro do plano. ERRO => {str(e)}")
    
def update_cobranca(db: Session, codcobranca: int, dados: schemas.CobrancaCreate):
    cobranca_db = db.query(models.Cobranca).filter(models.Cobranca.codcobranca == codcobranca).first()

    if not cobranca_db:
        return {
            "status": 404,
            "message": "Plano de pagamento não localizado",
            "success": False
        }
    
    try:
        cobranca_db.cobranca = dados.cobranca,
        cobranca_db.status = dados.status

        db.commit()
        db.refresh(cobranca_db)

        return {
            "status": 200,
            "message": "Cobrança atualizada com sucesso",
            "success": True,
            "data": cobranca_db
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível atualizar a cobrança. ERRO => {str(e)}")

def delete_plano(db: Session, codplano: int):
    try:
        plano_db = db.query(models.Plano).filter(models.Plano.codplano == codplano).first()

        if plano_db:
            db.delete(plano_db)
            db.commit()
            return {
                "status": 204,
                "message": "Plano de pagamento excluído com sucesso"
            }
        else:
            return {
                "status": 404,
                "message": "Plano de pagamento não encontrado"
            }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível excluir o plano de pagamento. ERRO => {str(e)}")
    
def delete_cobranca(db: Session, codcobranca: int):
    try:
        cobranca_db = db.query(models.Cobranca).filter(models.Cobranca.codcobranca == codcobranca).first()

        if cobranca_db:
            db.delete(cobranca_db)
            db.commit()
            return {
                "status": 204,
                "message": "Cobrança excluído com sucesso"
            }
        else:
            return {
                "status": 404,
                "message": "Cobrança não encontrada"
            }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Não foi possível excluir a cobrança. ERRO => {str(e)}")
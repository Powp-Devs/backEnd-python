from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import schemas, models 

def create_sector(db: Session, dados: schemas.SetorCreate):
    try:
        new_setor = models.Sector(
            setor = dados.setor
        )

        db.add(new_setor)
        db.flush()
        db.commit()

        db.refresh(new_setor)

        return {
            "status": 201,
            "message": "Setor cadastrado com sucesso",
            "data": new_setor
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=f"Erro ao cadastrar setor. ERRO => {str(e)}")
    
def getSector_paginate(db: Session, page: int = 1, per_page: int = 10):

    offset = (page - 1) * per_page
    total_setores = db.query(models.Sector).count()
    
    setores_db = db.query(models.Sector).offset(offset).limit(per_page).all()

    return {
        "status": 200,
        "message": "Listagem de setores cadastrados",
        "setor": setores_db, 
        "total": total_setores,
        "page": page,
        "per_page": per_page
    }

def inativar_sector(db: Session, codsetor: int):

    setor_db = db.query(models.Sector).filter(models.Sector.codsetor == codsetor).first()

    if not setor_db:
        return {    
            "status": 404,
            "message": "Setor não encontrado",
            "success": False
        }
    
    try:
        setor_db.status = 'I'
        db.commit()
        db.refresh(setor_db)

        return {
            "status": 200,
            "message": "Setor inativado com sucesso",
            "data": setor_db
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=f"Erro ao inativar o setor. ERRO => {str(e)}")

def delete_sector(db: Session, codsetor: int):
    try:
        sector = db.query(models.Sector).filter(models.Sector.codsetor == codsetor).first()

        if sector: 
            db.delete(sector)
            db.commit()
            return {
                "status": 204,
                "message": "Setor excluído com sucesso"
            }
        else: 
            return {
                "status": 404,
                "message": "Setor não encontrado"
            }

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Não foi possível excluir o setor. ERRO => {str(e)}")
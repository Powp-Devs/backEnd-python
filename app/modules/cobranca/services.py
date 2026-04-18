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
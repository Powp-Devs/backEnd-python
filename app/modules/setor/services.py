from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import schemas, models 

def create_sector(db: Session, dados: schemas.SetorCreate):
    try:
        new_setor = models.Setor(
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
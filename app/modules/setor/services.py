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
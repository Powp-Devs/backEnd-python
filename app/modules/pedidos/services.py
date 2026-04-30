from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.modules.util import schemas, models as model_util
from . import schemas, models 

def create_pedido(db: Session, pedido: schemas.PedidoCreate):
    try:
        new_pedido_cabecalho = models.PedidoCabecalho(
            
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar um novo pedido no sistema. ERRO => {str(e)}")
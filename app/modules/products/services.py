from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

from . import schemas, models

def create_produtct(db: Session, dados: schemas.ProdutoCreate):
    try:
        new_product = models.Produto(
            produto = dados.produto,
            sku = dados.sku,
            embalagem = dados.embalagem,
            unidade = dados.unidade,
            ean = dados.ean,
            gtin = dados.gtin,
            status = dados.status,
            dtcadastro = datetime.now()
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=f"Erro ao cadastrar um novo produto no sistema. ERRO => {str(e)}")
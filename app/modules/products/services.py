from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

from . import schemas, models

def create_product(db: Session, dados: schemas.ProdutoCreate):
    try:
        new_product = models.Produto(
            produto = dados.produto,
            sku = dados.sku,
            embalagem = dados.embalagem,
            unidade = dados.unidade,
            ean = dados.ean,
            gtin = dados.gtin,
            status = dados.status,
            codfornecedor = dados.codfornecedor,
            dtcadastro = datetime.now()
        )

        db.add(new_product)
        db.flush()

        new_price = models.Preco (
            codproduto = new_product.codproduto,
            preco_custo = dados.custo,
            preco_venda = dados.preco_venda,
            margem = dados.margem,
            dtcadastro = datetime.now()
        )

        db.add(new_price)
        db.flush()

        db.commit()
        db.refresh(new_price)

        return {
            "status": 201,
            "message": "Produto cadastrado e precificado com sucesso",
            "produto": new_product,
            "preco": new_price
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=f"Erro ao cadastrar um novo produto no sistema. ERRO => {str(e)}")
    
def delete_product(db: Session, product_id: int):
    produto_db = db.query(models.Produto).filter(models.Produto.codproduto == product_id).first()

    if not produto_db:
        return {
            "status": 404,
            "message": "Produto não encontrado",
            "success": False
        }
    
    

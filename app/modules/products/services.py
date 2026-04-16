from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

from . import schemas, models

def create_product(db: Session, dados: schemas.ProdutoCreate):
    try:
        new_price = models.Preco (
            preco_custo = dados.custo,
            preco_venda = dados.preco_venda,
            margem = dados.margem,
            dtcadastro = datetime.now()
        )

        db.add(new_price)
        db.flush()

        new_product = models.Produto(
            produto = dados.produto,
            sku = dados.sku,
            embalagem = dados.embalagem,
            unidade = dados.unidade,
            ean = dados.ean,
            gtin = dados.gtin,
            status = dados.status,
            codfornecedor = dados.codfornecedor,
            codpreco = new_price.codpreco,
            dtcadastro = datetime.now()
        )

        db.add(new_product)
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
    
#Ajustar o LOG de exclusão
def delete_product(db: Session, dados: schemas.ProdutoLogCreate):
    try:
        produto_db = db.query(models.Produto).filter(models.Produto.codproduto == dados.codproduto).first()

        if not produto_db:
            return {
                "status": 404,
                "message": "Produto não encontrado",
                "success": False
            }

        '''new_log = models.ProdutoLog(
            data = datetime.now(),
            codproduto = produto_db.codproduto,
            tipo = "DELETE",
            obs = dados.obs,
            cod_func_alter = dados.cod_func_alter
        )

        db.add(new_log)
        db.flush()'''

        id_preco = produto_db.codpreco

        db.delete()
        db.query(models.Preco).filter(models.Preco.codpreco == id_preco).delete()
        
        db.flush()
        db.commit()

        return {
            "status": 200,
            "message": "Produto excluído com sucesso",
            "success": True
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=f"Erro ao excluir o produto. ERRO => {str(e)}")
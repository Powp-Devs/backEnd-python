from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/produtos", tags=["Rotas de Produtos e Precificação"])

@router.get("/listar")
def listar_produtos(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getProduct_paginate(db=db, page=page, per_page=per_page)

@router.post("/cadastrar", summary="Rota para realizar o cadastro.", description="Rota para cadastrar os dados de um produto junto com a sua precificação inicial")
def cadastrar_product(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return services.create_product(db=db, dados=produto)

@router.delete("/excluir/{codproduto}", summary="Rota para excluir produto", description="Está rota faz com que chame uma função que exclui o item do sistema junto com a sua precificação. Esta rota será temporária!!!")
def excluir_prod(dados_exclusao: schemas.ProdutoLogCreate, db: Session = Depends(get_db)):
    return services.delete_product(db=db, dados=dados_exclusao)
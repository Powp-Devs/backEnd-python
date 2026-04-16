from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/produtos", tags=["Rotas de Produtos e Precificação"])

@router.post("/cadastrar", summary="Rota para realizar o cadastro.", description="Rota para cadastrar os dados de um produto junto com a sua precificação inicial")
def cadastrar_product(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return services.create_product(db=db, dados=produto)

@router.delete("/excluir", summary="Rota para excluir produto", description="Está rota faz com que chame uma função que exclui o item do sistema junto com a sua precificação. Esta rota será temporária!!!")
def excluir_prod(dados_exclusao: schemas.ProdutoLogCreate, db: Session = Depends(get_db)):
    return services.delete_product(db=db, dados=dados_exclusao)
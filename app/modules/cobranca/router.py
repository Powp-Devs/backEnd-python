from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/pagamento", tags=["Rotas para os planos e cobranças da empresa"])

@router.get("/listar/plano", summary="Rota para listar planos de pagamento", description="Rota para listar todos os planos de pagamento por meio de paginação")
def listar_planos(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getPlano_paginate(db=db, page=page, per_page=per_page)

@router.get("/listar/cobranca", summary="Rota para listar as cobranças", description="Rota para listar todas as cobranças por meio de paginação")
def listar_cobrancas(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.getCobranca_paginate(db=db, page=page, per_page=per_page)

@router.post("/cadastrar/plano", summary="Rota para cadastrar um novo plano da empresa", description="Rota redará uma função que cadastra novos planos de pagamento dentro da empresa")
def cadastrar_plano(dados_plano: schemas.PlanoCreate, db: Session = Depends(get_db)):
    return services.create_plano(db=db, dados=dados_plano)

@router.post("/cadastrar/cobranca", summary="Rota para cadastrar cobrança", description="Rota para cadastrar uma nova cobrança no sistema que será utilizado no sistema nas vendas.")
def cadastrar_cobranca(dados_cobranca: schemas.CobrancaCreate, db: Session = Depends(get_db)):
    return services.create_cobranca(db=db, dados=dados_cobranca)

@router.put("/atualizar/plano/{codplano}", summary="Rota para atualizar um plano de pagamento", description="Função que atualiza os dados cadastrais do plano de pagamento")
def atualizar_plano(codplano: int, dados: schemas.PlanoCreate, db: Session = Depends(get_db)):
    return services.update_plano(db=db, codplano=codplano, dados=dados)

@router.put("/atualizar/cobranca/{codcobranca}", summary="Rota para atualizar uma cobrança", description="Função que atualiza os dados cadastrais da cobrança no sistema.")
def atualizar_plano(codcobranca: int, dados: schemas.CobrancaCreate, db: Session = Depends(get_db)):
    return services.update_plano(db=db, codcobranca=codcobranca, dados=dados)


@router.put("/inativar/plano/{codplano}", summary="Rota para inativar um plano", description="Rota para inativar o plano no sistema, pois precisamos de log.")
def inativar_plano(codplano: int, db: Session = Depends(get_db)):
    return services.inativar_plano(db=db, codplano=codplano)

@router.put("/inativar/cobranca/{codcobranca}", summary="Rota para inativar uma cobrança", description="Rota para inativar a sobrança, pois precisamos de log.")
def inativar_cobranca(codcobranca: int, db: Session = Depends(get_db)):
    return services.inativar_cobranca(db=db, codcobranca=codcobranca)

@router.delete("/excluir/plano/{codplano}", summary="Rota para excluir o plano de pagamento", description="Rota para excluir o plano de pagamento cadastrado no sistema")
def excluir_plano(codplano: int, db: Session = Depends(get_db)):
    return services.delete_plano(db=db, codplano=codplano)

@router.delete("/excluir/cobranca/{codcobranca}", summary="Rota para excluir a cobrança.", description="Rota para excluir a cobrança cadastrado no sistema")
def excluir_cobranca(codcobranca: int, db: Session = Depends(get_db)):
    return services.delete_cobranca(db=db, codcobranca=codcobranca)
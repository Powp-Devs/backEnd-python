from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from . import schemas, services
from app.core.database import get_db

router = APIRouter(prefix="/fornecedor", tags=["Rotas de Fornecedores"])

@router.post("/cadastrar",status_code=status.HTTP_201_CREATED,summary="Cadastrar um novo fornecedor")
def create_fornec(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    return services.create_fornecedor(db=db, fornecedor=fornecedor)

@router.get("/listar",summary="Listar fornecedores com paginação")
def list_fornec(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return services.list_fornecedor(db=db, page=page, per_page=per_page)

# ── Rota que estava FALTANDO no backend ──────────────────────────────────────
@router.get("/{codfornec}",summary="Obter fornecedor por ID")
def get_fornec(codfornec: int, db: Session = Depends(get_db)):
    return services.get_fornecedor(db=db, codfornec=codfornec)

@router.put("/atualizar/{codfornec}",summary="Atualizar um fornecedor", )
def update_fornec(
    codfornec: int,
    fornecedor: schemas.FornecedorUpdate,
    db: Session = Depends(get_db),
):
    return services.update_fornecedor(db=db, codfornec=codfornec, fornecedor_update=fornecedor)

@router.delete("/excluir/{codfornec}", status_code=status.HTTP_200_OK, summary="Excluir um fornecedor",)
def delete_fornec(codfornec: int, db: Session = Depends(get_db)):
    return services.excluir_fornecedor(db=db, codfornec=codfornec)

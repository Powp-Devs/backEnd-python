from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import schemas as schemas_supplier, models as models
from app.modules.util import schemas, models as model_util


def create_fornecedor(db: Session, fornecedor: schemas_supplier.FornecedorCreate):
    try:
        new_endereco = model_util.Endereco(
            logradouro = fornecedor.logradouro,
            numero     = fornecedor.numero,
            cep        = fornecedor.cep,
            bairro     = fornecedor.bairro,
            cidade     = fornecedor.cidade,
            uf         = fornecedor.uf,
            pais       = fornecedor.pais,
        )

        new_contato = model_util.Contato(
            telefone = fornecedor.telefone,
            celular  = fornecedor.celular,
            email    = fornecedor.email,
            email2   = fornecedor.email2,
        )

        db.add(new_endereco)
        db.add(new_contato)
        db.flush()  # Gerar IDs antes de criar o fornecedor

        new_fornecedor = models.Fornecedor(
            fornecedor          = fornecedor.fornecedor,
            fantasia            = fornecedor.fantasia,
            cnpj                = fornecedor.cnpj,
            inscricaoestadual   = fornecedor.inscricaoestadual,
            tipopessoa          = fornecedor.tipopessoa,
            dtcadastro          = fornecedor.dtcadastro,
            obs                 = fornecedor.obs,
            bloqueio            = fornecedor.bloqueio,
            motivo_bloqueio     = fornecedor.motivo_bloqueio,
            dtbloqueio          = fornecedor.dtbloqueio,
            nome_representante  = fornecedor.nome_representante,
            cpf_representante   = fornecedor.cpf_representante,
            codtelefone         = new_contato.codcontato,
            codendereco         = new_endereco.codendereco,
        )

        db.add(new_fornecedor)
        db.commit()
        db.refresh(new_fornecedor)

        return {
            "code":    201,
            "message": "Fornecedor cadastrado com sucesso",
            "data":    new_fornecedor,
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=501, detail=f"Erro ao cadastrar fornecedor. ERRO => {str(e)}")


# ── GET by ID — estava FALTANDO ──────────────────────────────────────────────
def get_fornecedor(db: Session, codfornec: int):
    """
    Retorna um fornecedor com seus dados de endereço e contato aninhados.
    O frontend usa esta rota no modal de edição (openEditSupplierModal).
    """
    fornecedor = (
        db.query(models.Fornecedor)
        .filter(models.Fornecedor.codfornecedor == codfornec)
        .first()
    )

    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")

    endereco = (
        db.query(model_util.Endereco)
        .filter(model_util.Endereco.codendereco == fornecedor.codendereco)
        .first()
    )

    contato = (
        db.query(model_util.Contato)
        .filter(model_util.Contato.codcontato == fornecedor.codtelefone)
        .first()
    )

    return {
        "code": 200,
        "data": {
            **fornecedor.__dict__,
            "endereco": endereco.__dict__ if endereco else {},
            "contato":  contato.__dict__  if contato  else {},
        },
    }


def excluir_fornecedor(db: Session, codfornec: int):
    try:
        fornecedor = (
            db.query(models.Fornecedor)
            .filter(models.Fornecedor.codfornecedor == codfornec)
            .first()
        )

        if not fornecedor:
            raise HTTPException(status_code=404, detail="Fornecedor não encontrado")

        db.delete(fornecedor)
        db.commit()
        return {"code": 200, "message": "Fornecedor excluído com sucesso"}

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=501, detail=f"Erro ao excluir fornecedor. ERRO => {str(e)}")


def list_fornecedor(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    total  = db.query(models.Fornecedor).count()

    fornecedores = db.query(models.Fornecedor).offset(offset).limit(per_page).all()
    enderecos    = db.query(model_util.Endereco).all()
    contatos     = db.query(model_util.Contato).all()

    return {
        "fornecedor": fornecedores,
        "endereco":   enderecos,
        "contato":    contatos,
        "total":      total,
        "page":       page,
        "per_page":   per_page,
    }


def update_fornecedor(db: Session, codfornec: int, fornecedor_update: schemas_supplier.FornecedorUpdate):
    try:
        fornecedor = (
            db.query(models.Fornecedor)
            .filter(models.Fornecedor.codfornecedor == codfornec)
            .first()
        )

        if not fornecedor:
            raise HTTPException(status_code=404, detail="Fornecedor não encontrado")

        update_data = fornecedor_update.dict(exclude_unset=True)

        for key, value in update_data.items():
            if hasattr(fornecedor, key):
                setattr(fornecedor, key, value)

        if fornecedor.codendereco:
            endereco = (
                db.query(model_util.Endereco)
                .filter(model_util.Endereco.codendereco == fornecedor.codendereco)
                .first()
            )
            if endereco:
                for key in ['cep', 'logradouro', 'numero', 'bairro', 'cidade', 'uf', 'pais']:
                    if key in update_data:
                        setattr(endereco, key, update_data[key])

        if fornecedor.codtelefone:
            contato = (
                db.query(model_util.Contato)
                .filter(model_util.Contato.codcontato == fornecedor.codtelefone)
                .first()
            )
            if contato:
                for key in ['telefone', 'celular', 'email', 'email2']:
                    if key in update_data:
                        setattr(contato, key, update_data[key])

        db.commit()
        db.refresh(fornecedor)

        return {
            "code":    200,
            "message": "Fornecedor atualizado com sucesso",
            "data":    fornecedor,
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=501, detail=f"Erro ao atualizar fornecedor. ERRO => {str(e)}")

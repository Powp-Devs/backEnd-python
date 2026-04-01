from sqlalchemy.orm import Session
from . import schemas as schemas_supplier, models as models
from app.modules.util import schemas, models as model_util


def create_fornecedor(db: Session, fornecedor: schemas_supplier.FornecedorCreate):
    try:
        new_endereco = model_util.Endereco(
            logradouro = fornecedor.logradouro,
            numero = fornecedor.numero,
            cep = fornecedor.cep,
            bairro = fornecedor.bairro,
            cidade = fornecedor.cidade,
            uf = fornecedor.uf,
            pais = fornecedor.pais  
        )
        
        new_contato = model_util.Contato(
            telefone = fornecedor.telefone,
            celular = fornecedor.celular,
            email = fornecedor.email,
            email2 = fornecedor.email2
        )
        
        db.add(new_endereco)
        db.add(new_contato)
        db.flush() #Gerar os ID's 
        
        new_fornecedor = models.Fornecedor(
            fornecedor = fornecedor.fornecedor,
            fantasia = fornecedor.fantasia,
            cnpj = fornecedor.cnpj,
            inscricaoestadual = fornecedor.inscricaoestadual,
            tipopessoa = fornecedor.tipopessoa,
            dtcadastro = fornecedor.dtcadastro,
            obs = fornecedor.obs,
            bloqueio = fornecedor.bloqueio,
            motivo_bloqueio = fornecedor.motivo_bloqueio,
            dtbloqueio = fornecedor.dtbloqueio,
            nome_representante = fornecedor.nome_representante,
            cpf_representante = fornecedor.cpf_representante,
            codtelefone = new_contato.codcontato,
            codendereco = new_endereco.codendereco
        )
        
        db.add(new_fornecedor)
        db.commit()
        db.refresh(new_fornecedor)
        
        return {
            "code": 201,
            "message": "Fornecedor cadastrado com sucesso",
            "data": new_fornecedor
        }
        
    except Exception as e:
        db.rollback()
        raise e
    
def excluir_fornecedor(db: Session, codfornec: int):
    try: 
        fornecedor = db.query(models.Fornecedor).filter(models.Fornecedor.codfornecedor == codfornec).first()
        
        if fornecedor:
            db.delete(fornecedor)
            db.commit()
            return {
                "code": 200,
                "message": "Fornecedor excluído com sucesso"
            }
        else:
            return {
                "code": 404,
                "message": "Fornecedor não encontrado"
            }
    except Exception as e:
        db.rollback()
        raise e

def list_fornecedor(db: Session, page: int = 1, per_page: int = 10):
    
    offset = (page - 1) * per_page
    total_fornecedores = db.query(models.Fornecedor).count()
    
    fornecedores_db = db.query(models.Fornecedor).offset(offset).limit(per_page).all()
    endereco_db = db.query(model_util.Endereco).all()
    contato_db = db.query(model_util.Contato).all()

    return {
        "fornecedor": fornecedores_db, 
        "endereco": endereco_db,
        "contato": contato_db,
        "total": total_fornecedores,
        "page": page,
        "per_page": per_page
    }
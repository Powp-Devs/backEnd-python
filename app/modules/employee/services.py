from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.modules.util import schemas, models as model_util
from . import schemas, models 

def create_empregrado(db: Session, dados: schemas.EmpregadoCreate):
    try:
        new_endereco = model_util.Endereco(
            logradouro = dados.logradouro,
            numero = dados.numero,
            cep = dados.cep,
            bairro = dados.bairro,
            cidade = dados.cidade,
            uf = dados.uf,
            pais = dados.pais   
        )
        
        new_contato = model_util.Contato(
            telefone = dados.telefone,
            celular = dados.celular,
            email = dados.email,
            email2 = dados.email2
        )
        
        db.add(new_endereco)
        db.add(new_contato)
        db.flush()

        new_employee = models.Empregado(
            empregado = dados.empregado,
            cpf = dados.cpf,
            rg = dados.rg,
            data_nascimento = dados.data_nascimento,
            data_admissao = dados.data_admissao,
            data_demissao = dados.data_demissao,
            email_corporativo = dados.email_corporativo,
            obs = dados.obs,
            bloqueio = dados.bloqueio,
            motivo_bloq = dados.motivo_bloq,
            cargo = dados.cargo,
            salario = dados.salario,
            codsetor = dados.codsetor
        )

        if dados.salario <= 0:
            db.rollback()
            raise HTTPException(status_code=403, detail="O salário não pode ser menor ou igual a zero!")

        db.add(new_employee)
        db.flush()
        db.commit()

        db.refresh(new_employee)

        return {
            "status": 201,
            "message": "Empregado cadastrado com sucesso",
            "data": new_employee
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=f"Erro ao cadastrar empregado. ERRO => {str(e)}")
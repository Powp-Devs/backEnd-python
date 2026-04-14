from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.modules.util import schemas, models as model_util
from . import schemas, models 

def create_employee(db: Session, dados: schemas.EmpregadoCreate):
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
    
def getEmployee_paginate(db: Session, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    total_employee = db.query(models.Empregado).count

    employee_db = db.query(models.Empregado).offset(offset).limit(per_page).all()
    adress_db = db.query(model_util.Endereco).all()
    phone_db = db.query(model_util.Contato).all()

    return {
        "status": 201,
        "empregado": employee_db,
        "endereco": adress_db,
        "contato": phone_db,
        "total": total_employee,
        "page": page,
        "per_page": per_page 
    }


def delete_employee(db: Session, employee_id: int):

    employee_db = db.query(models.Empregado).filter(models.Empregado.codempregado == employee_id).first()

    if not employee_db: 
        return {
            "status": 404,
            "message": "Empregado não encontrado",
            "sucess": False
        }
    
    id_adress = employee_db.codendereco
    id_phone = employee_db.codtelefone

    db.delete(employee_db)
    db.flush()

    if id_adress:
        db.query(model_util.Endereco).filter(model_util.Endereco.codendereco == id_adress).delete()
    
    if id_phone:
        db.query(model_util.Contato).filter(model_util.Contato.codcontato == id_phone).delete()

    db.commit()

    return {
        "status": 200,
        "message": "Empregado excluído com sucesso",
        "success": True
    }
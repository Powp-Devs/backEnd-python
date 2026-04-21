from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.modules.util import schemas, models as model_util
from . import schemas, models 

def create_employee(db: Session, dados: schemas.EmpregadoCreate):
    try:
        if dados.salario <= 0:
            db.rollback()
            raise HTTPException(status_code=400, detail="O salário não pode ser menor ou igual a zero!")

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
            codsetor = dados.codsetor,
            codendereco = new_endereco.codendereco,
            codtelefone = new_contato.codcontato
        )

        db.add(new_employee)
        db.flush()
        db.commit()

        db.refresh(new_employee)

        return {
            "status": 201,
            "message": "Empregado cadastrado com sucesso",
            "data": new_employee
        }
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        print(f"Erro ao cadastrar empregado: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar empregado. ERRO => {str(e)}")
    
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

def get_employee_by_id(db: Session, codempregado: int):
    employee_db = db.query(models.Empregado).filter(models.Empregado.codempregado == codempregado).first()
    
    if not employee_db:
        raise HTTPException(status_code=404, detail="Empregado não encontrado")
    
    endereco = db.query(model_util.Endereco).filter(model_util.Endereco.codendereco == employee_db.codendereco).first() if employee_db.codendereco else None
    contato = db.query(model_util.Contato).filter(model_util.Contato.codcontato == employee_db.codtelefone).first() if employee_db.codtelefone else None
    
    return {
        "status": 200,
        "data": {
            **employee_db.__dict__,
            "endereco": endereco.__dict__ if endereco else None,
            "contato": contato.__dict__ if contato else None
        }
    }

def update_employee(db: Session, codempregado: int, dados: schemas.EmpregadoUpdate):
    empregado_db = db.query(models.Empregado).filter(models.Empregado.codempregado == codempregado).first()

    if not empregado_db:
        return {
            "status": 404,
            "message": "Funcionário não localizado",
            "success": False
        }

    try:
        empregado_db.empregado = dados.empregado
        empregado_db.cpf = dados.cpf
        empregado_db.rg = dados.rg
        empregado_db.data_nascimento = dados.data_nascimento
        empregado_db.data_admissao = dados.data_admissao
        empregado_db.data_demissao = dados.data_demissao
        empregado_db.email_corporativo = dados.email_corporativo
        empregado_db.obs = dados.obs
        empregado_db.bloqueio = dados.bloqueio
        empregado_db.motivo_bloq = dados.motivo_bloq
        empregado_db.cargo = dados.cargo
        empregado_db.salario = dados.salario
        empregado_db.codsetor = dados.codsetor
        empregado_db.codendereco = dados.codendereco
        empregado_db.codtelefone = dados.codcontato

        if empregado_db.codendereco:
            endereco_db = db.query(model_util.Endereco).filter(model_util.Endereco.codendereco == empregado_db.codendereco).first()
            if endereco_db:
                endereco_db.logradouro = dados.logradouro
                endereco_db.numero = dados.numero
                endereco_db.cep = dados.cep
                endereco_db.bairro = dados.bairro
                endereco_db.cidade = dados.cidade
                endereco_db.uf = dados.uf
                endereco_db.pais = dados.pais
        else:
            return {
                "code": 404,
                "message": "Endereço não encontrado",
                "success": False
            }

        if empregado_db.codtelefone:
            contato_db = db.query(model_util.Contato).filter(model_util.Contato.codcontato == empregado_db.codtelefone).first()
            if contato_db:
                contato_db.telefone = dados.telefone
                contato_db.celular = dados.celular
                contato_db.email = dados.email
                if hasattr(dados, 'email2'):
                    contato_db.email2 = dados.email2
        else: 
            return {
                "code": 404,
                "message": "Contato não encontrado",
                "success": False
            }
        
        db.commit()
        db.refresh(empregado_db)

        return {
            "status": 201,
            "message": "Funcionário atualizado com sucesso",
            "success": True,
            "data": empregado_db
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar o cliente. ERRO => {str(e)}")

def delete_employee(db: Session, codempregado: int):

    employee_db = db.query(models.Empregado).filter(models.Empregado.codempregado == codempregado).first()

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
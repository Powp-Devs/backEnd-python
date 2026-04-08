from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date 
from typing import Literal, Optional

class EmpregadoCreate(BaseModel):
    #Campos PWEMPREGADO
    empregado: str = Field(..., max_length=255)
    cpf: str = Field(None, max_length=14)
    rg: str = Field(None, max_length=20) 
    data_nascimento: date 
    data_admissao: date 
    data_demissao: Optional[date] = None
    email_corporativo: EmailStr = Field(None, max_length=150)
    obs: Optional[str]  = Field(None, max_length=255)
    bloqueio: str = constr(min_length=1, max_length=1)
    motivo_bloq: Optional[str] = None
    cargo: str = Field(None, max_length=100)
    salario: float = Field(..., gt=0)
    codsetor: int

    #Campos PWENDERECO
    cep: str = Field(..., max_length=9)
    logradouro: str = Field(..., max_length=255)
    numero: Optional[str] = Field(None, max_length=10)
    bairro: str = Field(..., max_length=80)
    cidade: str = Field(..., max_length=50)
    uf: str = Field(None, min_length=2, max_length=2)
    pais: str = Field("BR", min_length=2, max_length=2)
    
    #Campos PWCONTATO
    telefone: str = Field(None, max_length=20)
    celular: str = Field(None, max_length=20)
    email: EmailStr = Field(None, max_length=150)
    email2: Optional[EmailStr] = Field(None, max_length=150)
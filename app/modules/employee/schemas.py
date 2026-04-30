from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date 
from typing import Optional

class EmpregadoCreate(BaseModel):
    #Campos PWEMPREGADO
    empregado: str = Field(..., max_length=255)
    cpf: Optional[str] = Field(None, max_length=14)
    rg: Optional[str] = Field(None, max_length=20) 
    data_nascimento: date 
    data_admissao: date 
    data_demissao: Optional[date] = None
    email_corporativo: Optional[str] = Field(None, max_length=150)
    obs: Optional[str] = Field(None, max_length=255)
    bloqueio: str = Field(default='N', min_length=1, max_length=1)
    motivo_bloq: Optional[str] = None
    cargo: Optional[str] = Field(None, max_length=100)
    salario: float = Field(..., gt=0)
    codsetor: int

    #Campos PWENDERECO
    cep: str = Field(..., max_length=9)
    logradouro: str = Field(..., max_length=255)
    numero: Optional[str] = Field(None, max_length=10)
    bairro: str = Field(..., max_length=80)
    cidade: str = Field(..., max_length=50)
    uf: Optional[str] = Field(None, min_length=2, max_length=2)
    pais: str = Field(default="BR", min_length=2, max_length=2)
    
    #Campos PWCONTATO
    telefone: Optional[str] = Field(None, max_length=20)
    celular: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = Field(None, max_length=150)
    email2: Optional[str] = Field(None, max_length=150)

class EmpregadoUpdate(BaseModel):
    #Campos PWEMPREGADO
    empregado: str = Field(..., max_length=255)
    cpf: Optional[str] = Field(None, max_length=14)
    rg: Optional[str] = Field(None, max_length=20) 
    data_nascimento: date 
    data_admissao: date 
    data_demissao: Optional[date] = None
    email_corporativo: Optional[str] = Field(None, max_length=150)
    obs: Optional[str] = Field(None, max_length=255)
    bloqueio: str = Field(default='N', min_length=1, max_length=1)
    motivo_bloq: Optional[str] = None
    cargo: Optional[str] = Field(None, max_length=100)
    salario: float = Field(..., gt=0)
    codsetor: int

    #Campos PWENDERECO
    codendereco: int
    cep: str = Field(..., max_length=9)
    logradouro: str = Field(..., max_length=255)
    numero: Optional[str] = Field(None, max_length=10)
    bairro: str = Field(..., max_length=80)
    cidade: str = Field(..., max_length=50)
    uf: Optional[str] = Field(None, min_length=2, max_length=2)
    pais: str = Field(default="BR", min_length=2, max_length=2)
    
    #Campos PWCONTATO
    codcontato: int
    telefone: Optional[str] = Field(None, max_length=20)
    celular: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = Field(None, max_length=150)
    email2: Optional[str] = Field(None, max_length=150)
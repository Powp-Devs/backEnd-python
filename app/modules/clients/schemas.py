from pydantic import BaseModel, EmailStr, Field, constr 
from datetime import date
from typing import Literal, Optional 

class ClienteCreate(BaseModel):
    #Campos PWCLIENTE 
    cliente: str = Field(..., max_length=255)
    fantasia: Optional[str] = Field(None, max_length=255)
    email: EmailStr = Field(..., max_length=255)
    obs: Optional[str] = Field(None, max_length=255)
    bloqueio: constr(min_length=1, max_length=1)
    motivo_bloq: Optional[str] = None
    tipopessoa: Literal['F', 'J']

    #Campos PWCLIENTE_FISICO
    cpf: Optional[constr(min_length=11, max_length=11)] = None
    rg: Optional[str] = Field(None, max_length=20)
    dt_nascimento: Optional[date] = None
     
    #Campos PWCLIENTE_JURIDICO
    cnpj: Optional[constr(min_length=14, max_length=14)] = None
    inscricaoestadual: Optional[str] = Field(None, max_length=20)
    dtabertura: Optional[date] = None

    #Campos PWENDERECO
    cep: str = Field(..., max_length=9)
    logradouro: str = Field(..., max_length=255)
    numero: Optional[str] = Field(..., max_length=10)
    bairro: str = Field(..., max_length=80)
    cidade: str = Field(..., max_length=50)
    estado: Optional[constr(min_length=2, max_length=2)] = None
    
    #Campos PWCONTATO
    telefone: Optional[str] = Field(None, max_length=20)
    celular: Optional[str] = Field(None, max_length=20)
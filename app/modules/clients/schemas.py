from pydantic import BaseModel, EmailStr, Field, constr 
from datetime import date
from typing import Literal, Optional 

class ClienteCreate(BaseModel):
    #Campos PWCLIENTE 
    cliente: str = Field(..., max_length=255)
    fantasia: Optional[str] = Field(None, max_length=255)
    dtcadastro: date = Field(...)
    tipopessoa: Literal['F', 'J']
    obs: Optional[str] = Field(None, max_length=255)
    bloqueio: str = constr(min_length=1, max_length=1)
    motivo_bloq: Optional[str] = None

    #Campos PWCLIENTE_FISICO
    cpf: Optional[str] = Field(None, max_length=11)
    rg: Optional[str] = Field(None, max_length=20)
    dt_nascimento: Optional[date] = None
     
    #Campos PWCLIENTE_JURIDICO
    cnpj: Optional[str] = Field(None, max_length=14)
    inscricaoestadual: Optional[str] = Field(None, max_length=20)
    dtabertura: Optional[date] = None

    #Campos PWENDERECO
    cep: str = Field(..., max_length=9)
    logradouro: str = Field(..., max_length=255)
    numero: Optional[str] = Field(..., max_length=10)
    bairro: str = Field(..., max_length=80)
    cidade: str = Field(..., max_length=50)
    uf: str = Optional[constr(min_length=2, max_length=2)] 
    pais: str = constr(min_length=2, max_length=2)
    
    #Campos PWCONTATO
    telefone: str = Field(None, max_length=20)
    celular: str = Field(None, max_length=20)
    email: EmailStr = Field(None, max_length=150)
    email2: Optional[EmailStr] = Field(None, max_length=150)
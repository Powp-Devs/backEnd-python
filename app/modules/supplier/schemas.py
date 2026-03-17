from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date
from typing import Literal, Optional

class FornecedorCreate(BaseModel):
    #Campos PWFORNECEDOR
    fornecedor: str = Field(..., max_length=255)
    fantasia: str = Field(..., max_length=255)
    cnpj: str = Field(..., max_length=14)
    inscricaoestadual: str = Field(..., max_length=20)
    tipopessoa: Literal['F', 'J']
    dtcadastro: date
    obs: Optional[str] = Field(None, max_length=255)
    bloqueio: str = constr(min_length=1, max_length=1)
    motivo_bloqueio: Optional[str] = None
    dtbloqueio: Optional[date] = None
    nome_representante: Optional[str] = Field(None, max_length=255)
    cpf_representante: Optional[str] = Field(None, max_length=11)
    
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
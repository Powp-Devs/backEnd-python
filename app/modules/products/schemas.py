from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date
from typing import Literal, Optional

class ProdutoCreate(BaseModel):
    #Campos PWPRODUTO
    produto: str = Field(..., max_length=255)
    sku: str = Field(..., max_length=20)
    embalagem: str = Field(..., max_length=255)
    unidade: str = Field(..., max_length=10)
    gtin: str = Field(..., max_length=3)
    ean: str = Field(..., max_length=13)
    status: Literal['A', 'I']
    obs: Optional[str] = Field(None, max_length=255)
    dtalteracao = Optional[date] = None

    #Campos PWESTOQUE
    qtest: int
    qtbloqueada: int
    qtminima: int 
    
    #Campos PWTABPR
    custo: float
    preco_venda: float
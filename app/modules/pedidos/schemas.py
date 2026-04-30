from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date 
from typing import Optional

class PedidoCreate(BaseModel):
    #Campos PWPEDIDOC
    codcliente: int
    codcobranca: int
    codplano: int
    codvendedor: int
    obs: Optional[str] = Field(None, max_length=255)

    #Campos PWPEDIDOI
    codproduto: int
    quantidade: float = Field(..., gt=0)
    valor_venda: float = Field(..., gt=0)
    desconto: float = Field(..., gt=0)
from pydantic import BaseModel, Field
from datetime import date 
from typing import Literal, Optional

class PlanoCreate(BaseModel):
    plano: str = Field(..., max_length=255)
    status: Literal['A', 'I']
    numdias: int 
    prazo1: Optional[int]
    prazo2: Optional[int]
    prazo3: Optional[int]
    prazo4: Optional[int]
    prazo5: Optional[int]
    prazo6: Optional[int]

class CobrancaCreate(BaseModel):
    cobranca: str = Field(..., max_length=255)
    status: Literal['A', 'I']
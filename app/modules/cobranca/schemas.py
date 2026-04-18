from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date 
from typing import Literal, Optional

class PlanoCreate(BaseModel):
    plano: str = Field(..., max_length=255)
    numdias: int 
    prazo1: Optional[int]
    prazo2: Optional[int]
    prazo3: Optional[int]
    prazo4: Optional[int]
    prazo5: Optional[int]
    prazo6: Optional[int]

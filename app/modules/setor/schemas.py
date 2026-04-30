from pydantic import BaseModel, EmailStr, Field, constr
from datetime import date 
from typing import Literal, Optional

class SetorCreate(BaseModel):
    setor: str = Field(..., max_length=255)
    status: Literal['A', 'I']


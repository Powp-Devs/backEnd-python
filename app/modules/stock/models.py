from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Produto(Base):
    __tablename__ = "pwproduto"

    codproduto = Column(Integer, primary_key=True, index=True)

    produto = Column(String(255), nullable=False)
    embalagem = Column(String(20))
    ean = Column(String(10))
    dtcadastro = Column(Date)

    codfornecedor = Column(Integer, ForeignKey("pwfornecedor"))
    codpreco = Column(Integer, ForeignKey("pwpreco"))
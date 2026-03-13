from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Endereco(Base):
    __tablename__ = "pwfornecedor"

    codfornecedor = Column(Integer, primary_key=True, index=True)

    fornecedor = Column(String(255), nullable=False)
    fantasia = Column(String(255))
    cnpj = Column(String(20))
    dtcadastro = Column(Date)
    representante = Column(String(255))

    codendereco = Column(Integer, ForeignKey("pwendereco.codendereco"))
    codtelefone = Column(Integer, ForeignKey("pwcontato.codcontato"))
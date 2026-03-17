from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Fornecedor(Base):
    __tablename__ = "pwfornecedor"

    codfornecedor = Column(Integer, primary_key=True, index=True)

    fornecedor = Column(String(255), nullable=False)
    fantasia = Column(String(255))
    cnpj = Column(String(20))
    inscricaoestadual = Column(String(20))
    tipopessoa = Column(String(1))
    dtcadastro = Column(Date)
    obs = Column(Text)
    bloqueio = Column(String(1), nullable=False)    
    motivo_bloqueio = Column(Text)
    dtbloqueio = Column(Date)
    nome_representante = Column(String(255))
    cpf_representante = Column(String(11))

    codendereco = Column(Integer, ForeignKey("pwendereco.codendereco"))
    codtelefone = Column(Integer, ForeignKey("pwcontato.codcontato"))
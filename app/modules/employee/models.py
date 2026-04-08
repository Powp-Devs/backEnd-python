from sqlalchemy import Column, Integer, String, Date, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Empregado(Base):
    __tablename__ = 'pwempregado'

    codempregado = Column(Integer, primary_key=True, index=True)

    empregado = Column(String(255), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    rg = Column(String(20), unique=True)
    data_nascimento = Column(Date)
    data_admissao = Column(Date)
    data_demissao = Column(Date, nullable=True)
    email_corporativo = Column(String(255))
    obs = Column(Text)
    bloqueio = Column(String(1), default='N')
    motivo_bloq = Column(String(255))
    cargo = Column(String(100))
    salario = Column(Numeric(12,2))

    codsetor = Column(Integer, ForeignKey("pwsetor.codsetor"))
    codendereco = Column(Integer, ForeignKey("pwendereco.codendereco"))
    codtelefone = Column(Integer, ForeignKey("pwcontato.codcontato"))
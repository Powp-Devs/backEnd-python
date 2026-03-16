from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Cliente(Base): 
    __tablename__ = "pwcliente"

    codcliente = Column(Integer, primary_key = True, index=True)

    cliente = Column(String(255), nullable=False)
    fantasia = Column(String(255))
    dtcadastro = Column(Date)
    tipopessoa = Column(String(1)) #Opções F => Fisica e J => Juridica
    obs = Column(Text)
    bloqueio = Column(String(1), default='N')
    motivo_bloq = Column(String(255))

    pessoa_fisica = relationship("ClienteFisico")
    pessoa_juridica = relationship("ClienteJuridico")

    codendereco = Column(Integer, ForeignKey("pwendereco.codendereco"))
    codtelefone = Column(Integer, ForeignKey("pwcontato.codcontato"))

class ClienteFisico(Base):
    __tablename__ = "pwclientefisico"

    codcli= Column(Integer, ForeignKey("pwcliente.codcliente"), primary_key=True)

    cpf = Column(String(14))
    rg = Column(String(20))
    dt_nascimento = Column(Date)

class ClienteJuridico(Base):
    __tablename__ = "pwclientejuridico"

    codcli= Column(Integer, ForeignKey("pwcliente.codcliente"), primary_key=True)

    cnpj = Column(String(20))
    ie = Column(String(20)) #Inscrição Estadual
    dtabertura = Column(Date)
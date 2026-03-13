from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Endereco(Base):
    __tablename__ = "pwendereco"

    codendereco = Column(Integer, primary_key=True, index=True)

    logradouro = Column(String(255), nullable=False)
    numero = Column(String(20))
    cep = Column(String(10))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(String(2))
    pais = Column(String(2))

class Contato(Base):
    __tablename__ = "pwcontato"

    codcontato = Column(Integer, primary_key=True, index=True)
    telefone = Column(String(15))
    celular = Column(String(15))
    fax = Column(String(15))
    email = Column(String(100))
    email2 = Column(String(100), nullable=True)

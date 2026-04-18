from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Cobranca(Base):
    __tablename__ = 'pwcobranca'

    codcobranca = Column(Integer, primary_key=True, index=True)
    setor = Column(String(255), nullable=False)
    status = Column(String(1))

class Plano(Base):
    __tablename__ = 'pwplanopagamento'

    codplano = Column(Integer, primary_key=True, index=True)
    plano = Column(String(255), nullable=False)
    numdias = Column(Integer)
    prazo1 = Column(Integer)
    prazo2 = Column(Integer)
    prazo3 = Column(Integer)
    prazo4 = Column(Integer)
    prazo5 = Column(Integer)
    prazo6 = Column(Integer)

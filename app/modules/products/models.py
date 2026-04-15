from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Produto(Base):
    __tablename__ = "pwproduto"

    codproduto = Column(Integer, primary_key=True, index=True)

    produto = Column(String(255), nullable=False)
    sku = Column(String(20))
    embalagem = Column(String(20))
    unidade = Column(String(10))
    ean = Column(String(20))
    gtin = Column(String(10))
    status = Column(String(1), default="A")
    obs = Column(String(255))
    dtcadastro = Column(DateTime, default=datetime.now)
    dtalteracao = Column(DateTime, nullable=True)

    codfornecedor = Column(Integer, ForeignKey("pwfornecedor.codfornecedor"), nullable=False)
    codpreco = Column(Integer, ForeignKey("pwtabpr.codpreco"))

class Preco(Base):
    __tablename__ = "pwtabpr"

    codpreco = Column(Integer, primary_key=True, index=True)

    #codproduto = Column(Integer, ForeignKey("pwproduto.codproduto"))
    preco_custo = Column(Numeric(12,2))
    preco_venda = Column(Numeric(12,2))
    margem = Column(Numeric(12,2))
    
    dtcadastro = Column(DateTime, default=datetime.now)
    dtalteracao = Column(DateTime, nullable=True)
    cod_func_alter = Column(Integer, nullable=True)

class PrecoLog(Base):
    __tablename__ = "pwtabpr_log"

    codLog = Column(Integer, primary_key=True, index=True)

    codproduto = Column(Integer)
    custo_ant = Column(Numeric(12,2))
    custo_new = Column(Numeric(12,2))
    venda_ant = Column(Numeric(12,2))
    venda_new = Column(Numeric(12,2))
    margem_ant = Column(Numeric(12,2))
    margem_new = Column(Numeric(12,2))
    cod_func_alter = Column(Integer)
    
    data = Column(DateTime, default=datetime.now)
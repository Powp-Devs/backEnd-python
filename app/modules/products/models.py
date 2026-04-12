from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey, Numeric
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
    dtcadastro = Column(datetime, default=datetime.now)
    dtalteracao = Column(datetime, nullable=False)

    codfornecedor = Column(Integer, ForeignKey("pwfornecedor.codfornecedor"))
    codpreco = Column(Integer, ForeignKey("pwtabpr.codpreco"))

class Preco(Base):
    __tablename__ = "pwtabpr"

    codpreco = Column(Integer, primary_key=True, index=True)

    codproduto = Column(Integer, ForeignKey("pwproduto.codproduto"))
    preco_custo = Column(Numeric(12,2))
    preco_venda = Column(Numeric(12,2))
    margem = Column(Numeric(12,2))
    dtcadastro = Column(datetime, default=datetime.now)
    dtalteracao = Column(datetime, nullable=False)
    cod_func_alter = Column(Integer, nullable=False)


class PrecoLog(Base):
    __tablename__ = "pwtabpr_log"

    codproduto = Column(Integer, ForeignKey('pwproduto.codprod'))
    custo_ant = Column(Numeric(12,2))
    custo_new = Column(Numeric(12,2))
    venda_ant = Column(Numeric(12,2))
    venda_new = Column(Numeric(12,2))
    margem_ant = Column(Numeric(12,2))
    margem_new = Column(Numeric(12,2))
    cod_func_alter = Column(Integer)
    data = Column(datetime, default=datetime.now)
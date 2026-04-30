from sqlalchemy import Column, Integer, String, Date, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class PedidoCabecalho(Base):
    __tablename__ = 'pwpedidoc'

    codpedido = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    codcliente = Column(Integer, ForeignKey("pwcliente.codcliente"))
    codcobranca = Column(Integer, ForeignKey("pwcobranca.codcobranca"))
    codplano = Column(Integer, ForeignKey("pwplanopagamento.codplano"))
    qtdprodutos = Column(Integer)
    valor_total = Column(Numeric(12,2))
    valor_desconto = Column(Numeric(12,2))
    codvendedor = Column(Integer, ForeignKey("pwempregado.codempregado"))
    status = Column(String(1))
    obs = Column(Text)

class PedidoItens(Base):
    __tablename__ = 'pwpedidoi'

    codpedido = Column(Integer, ForeignKey("pwpedidoc.codpedido"))
    data = Column(Date, nullable=False)
    codproduto = Column(Integer, ForeignKey("pwproduto.codproduto"))
    quantidade = Column(Numeric(12,2))
    valor_tabela = Column(Numeric(12,2))
    valor_venda = Column(Numeric(12,2))
    valor_total = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    valor_desconto = Column(Numeric(12,2))
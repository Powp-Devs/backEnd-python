from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Sector(Base):
    __tablename__ = 'pwsetor'

    codsetor = Column(Integer, primary_key=True, index=True)
    setor = Column(String(255), nullable=False)

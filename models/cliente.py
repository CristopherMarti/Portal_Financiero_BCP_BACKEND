# models/cliente.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente  = Column(Integer, primary_key=True, index=True)
    codcliente  = Column(String(15), unique=True, nullable=False)
    nombres     = Column(String(150), nullable=False)
    dni         = Column(String(8), unique=True, nullable=False)
    email       = Column(String(100))

    usuario_hb  = relationship("UsuarioHomebanking", back_populates="cliente", uselist=False)
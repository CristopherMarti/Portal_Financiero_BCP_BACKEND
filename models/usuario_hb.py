# models/usuario_hb.py
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UsuarioHomebanking(Base):
    __tablename__ = "usuarios_homebanking"

    id_usuario        = Column(Integer, primary_key=True, index=True)
    cliente_id        = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    username          = Column(String(50), unique=True, nullable=False)
    password_hash     = Column(String(255), nullable=False)
    activo            = Column(String(1), default='S')
    bloqueado         = Column(String(1), default='N')
    intentos_fallidos = Column(SmallInteger, default=0)

    cliente = relationship("Cliente", back_populates="usuario_hb")
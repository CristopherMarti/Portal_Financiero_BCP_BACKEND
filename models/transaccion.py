from sqlalchemy import Column, Integer, String, Numeric, DateTime
from database import Base
from datetime import datetime

class Transaccion(Base):
    __tablename__ = "transacciones"

    id_transaccion = Column(Integer, primary_key=True, index=True)
    cuenta_id = Column(Integer, index=True)
    cliente_id = Column(Integer, index=True)
    tipo = Column(String(10)) 
    descripcion = Column(String(100))
    monto = Column(Numeric(14, 2))
    fecha = Column(DateTime, default=datetime.utcnow)
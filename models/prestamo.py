from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Prestamo(Base):
    __tablename__ = "prestamos"

    id_prestamo = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, index=True)
    proposito = Column(String(50))
    plazo_meses = Column(Integer)
    monto = Column(Numeric(14, 2))
    saldo_pendiente = Column(Numeric(14, 2))
    estado = Column(String(20))
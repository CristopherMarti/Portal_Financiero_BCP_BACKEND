from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Cuenta(Base):
    __tablename__ = "cuentas"

    id_cuenta = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, index=True)
    numero_cuenta = Column(String(20))
    tipo = Column(String(30)) # 'corriente' o 'ahorro'
    moneda = Column(String(3), default="PEN")
    saldo = Column(Numeric(14, 2))
    estado = Column(String(20))
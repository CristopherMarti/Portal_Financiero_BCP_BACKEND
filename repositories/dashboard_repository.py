from sqlalchemy.orm import Session
from models.cuenta import Cuenta
from models.prestamo import Prestamo
from models.transaccion import Transaccion

class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_resumen_cliente(self, cliente_id: int):
        # 1. Buscar cuentas
        cuentas = self.db.query(Cuenta).filter(Cuenta.cliente_id == cliente_id).all()
        
        # 2. Buscar préstamos
        prestamos = self.db.query(Prestamo).filter(Prestamo.cliente_id == cliente_id).all()
        
        # 3. Buscar movimientos usando el id_cuenta correcto
        cuenta_ids = [c.id_cuenta for c in cuentas]
        if cuenta_ids:
            txns = self.db.query(Transaccion).filter(Transaccion.cuenta_id.in_(cuenta_ids))\
                             .order_by(Transaccion.fecha.desc()).limit(5).all()
        else:
            txns = []
            
        return {
            "cuentas": cuentas,
            "prestamos": prestamos,
            "txns": txns
        }
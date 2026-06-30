from sqlalchemy.orm import Session
from repositories.dashboard_repository import DashboardRepository

class DashboardService:
    def __init__(self, db: Session):
        self.repo = DashboardRepository(db)

    def obtener_resumen(self, cliente_id: int):
        data = self.repo.obtener_resumen_cliente(cliente_id)
        
        return {
            "success": True,
            "data": {
                "cuentas": [
                    {"id": c.id_cuenta, "numero_cuenta": c.numero_cuenta, "tipo": c.tipo, "saldo": float(c.saldo)} 
                    for c in data["cuentas"]
                ],
                "prestamos": [
                    # Usamos getattr de forma segura por si el ID de préstamo tiene otro nombre
                    {"id": getattr(p, 'id', getattr(p, 'id_prestamo', 1)), "proposito": getattr(p, 'proposito', 'Crédito'), "plazo_meses": getattr(p, 'plazo_meses', 12), "saldo_pendiente": float(p.saldo_pendiente)} 
                    for p in data["prestamos"]
                ],
                "txns": [
                    {"id": t.id_transaccion, "tipo": t.tipo, "descripcion": t.descripcion, "monto": float(t.monto), "fecha": t.fecha.isoformat() if t.fecha else None} 
                    for t in data["txns"]
                ]
            }
        }
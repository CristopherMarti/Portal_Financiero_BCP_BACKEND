from sqlalchemy.orm import Session
from models.ahorro import Ahorro  # Asegúrate de tener este modelo mapeado

class AhorroRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_cuenta_ahorro(self, user_id: str):
        # ANTES: supabase.table("cuentas_ahorro")...
        # AHORA:
        return self.db.query(Ahorro).filter(Ahorro.user_id == user_id).first()

    def obtener_movimientos(self, user_id: str, cuenta_id: str):
        # AHORA:
        return self.db.query(Transaccion).filter(
            Transaccion.user_id == user_id, 
            Transaccion.cuenta_id == cuenta_id
        ).order_by(Transaccion.fecha.desc()).limit(10).all()
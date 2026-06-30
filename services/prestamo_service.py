# services/prestamo_service.py
from sqlalchemy.orm import Session
from repositories.prestamo_repository import PrestamoRepository

class PrestamoService:
    def __init__(self, db: Session):
        self.repo = PrestamoRepository(db)

    def crear_nueva_solicitud(self, data: dict):
        # Forzamos que si viene el monto, se asigne de inmediato al saldo inicial
        if "monto" in data and data["monto"] is not None:
            data["saldo_pendiente"] = data["monto"]
            
        if "estado" not in data or not data["estado"]:
            data["estado"] = "pendiente"

        return self.repo.crear_prestamo(data)
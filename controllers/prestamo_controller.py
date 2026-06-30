from sqlalchemy.orm import Session
from services.prestamo_service import PrestamoService

class PrestamoController:
    def __init__(self, db: Session):
        self.service = PrestamoService(db)

    def procesar_solicitud(self, datos: dict):
        return self.service.solicitar_nuevo_prestamo(datos)
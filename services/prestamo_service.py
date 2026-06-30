from sqlalchemy.orm import Session
from repositories.prestamo_repository import PrestamoRepository

class PrestamoService:
    def __init__(self, db: Session):
        # Aquí conectamos el repositorio pasándole la sesión
        self.repo = PrestamoRepository(db)

    def crear_nueva_solicitud(self, data: dict):
        # Aquí podrías añadir lógica extra (ej. validar si el cliente existe)
        return self.repo.crear_prestamo(data)
from sqlalchemy.orm import Session
from repositories.prestamo_repository import PrestamoRepository

class PrestamoService:
    def __init__(self, db: Session):
        # Aquí conectamos el repositorio pasándole la sesión
        self.repo = PrestamoRepository(db)

    def crear_nueva_solicitud(self, data: dict):
        # Lógica extra: Validar si viene el monto y asignar el saldo_pendiente inicial
        if "monto" in data and data["monto"] is not None:
            data["saldo_pendiente"] = data["monto"]
            
        # Opcional: Asegurar que el estado inicial siempre sea pendiente si no viene del front
        if "estado" not in data or not data["estado"]:
            data["estado"] = "pendiente"

        return self.repo.crear_prestamo(data)
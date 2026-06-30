from sqlalchemy.orm import Session
# Asegúrate de importar tu modelo de la base de datos
from models.prestamo import Prestamo 

class PrestamoRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear_prestamo(self, prestamo_data: dict):
        # Creamos el registro en PostgreSQL
        nuevo_prestamo = Prestamo(**prestamo_data)
        self.db.add(nuevo_prestamo)
        self.db.commit()
        self.db.refresh(nuevo_prestamo)
        return nuevo_prestamo
        
    def obtener_todos(self):
        return self.db.query(Prestamo).all()
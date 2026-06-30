from sqlalchemy.orm import Session
from models.prestamo import SolicitudPrestamo # Ajusta según tu nombre de modelo

class CreditosRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_todas_solicitudes(self):
        return self.db.query(SolicitudPrestamo).order_by(SolicitudPrestamo.created_at.desc()).all()

    def obtener_solicitud_por_id(self, solicitud_id: int):
        return self.db.query(SolicitudPrestamo).filter(SolicitudPrestamo.id == solicitud_id).first()

    def cambiar_estado(self, solicitud_id: int, nuevo_estado: str, comentario: str = None):
        prestamo = self.db.query(SolicitudPrestamo).filter(SolicitudPrestamo.id == solicitud_id).first()
        if prestamo:
            prestamo.estado = nuevo_estado
            if comentario:
                prestamo.comentario = comentario
            self.db.commit()
            self.db.refresh(prestamo)
        return prestamo
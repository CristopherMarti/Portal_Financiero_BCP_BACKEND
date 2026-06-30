from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.dashboard_service import DashboardService

router = APIRouter()

@router.get("/resumen/{cliente_id}")
def obtener_resumen_dashboard(cliente_id: int, db: Session = Depends(get_db)):
    service = DashboardService(db)
    return service.obtener_resumen(cliente_id)
from fastapi import APIRouter, Depends, HTTPException # 1. Importamos HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.prestamo_service import PrestamoService

router = APIRouter()

@router.post("/solicitar")
def solicitar_prestamo(data: dict, db: Session = Depends(get_db)):
    try:
        # Inicializamos el servicio con la sesión de la base de datos
        service = PrestamoService(db)
        
        # Procesamos la solicitud
        resultado = service.crear_nueva_solicitud(data)
        
        # 2. Verificamos que el resultado no sea nulo antes de acceder a .id_prestamo
        if not resultado:
             raise HTTPException(status_code=400, detail="No se pudo registrar la solicitud.")
             
        return {
            "success": True, 
            "mensaje": "Préstamo registrado correctamente", 
            "id": resultado.id_prestamo
        }
        
    except Exception as e:
        # 3. Manejo de errores para que el backend no colapse
        print(f"Error en endpoint solicitar_prestamo: {e}")
        raise HTTPException(status_code=500, detail=str(e))
# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from services.auth_service import AuthService
from pydantic import BaseModel

router = APIRouter()

class LoginSchema(BaseModel):
    username: str   # codcliente: ej. cli000007
    dni:      str   # 8 dígitos: ej. 12345677
    password: str   # clave: ej. demo1234

@router.post("/login")
def login(datos: LoginSchema, db: Session = Depends(get_db)):
    service   = AuthService(db)
    resultado = service.autenticar_usuario(datos.username, datos.dni, datos.password)

    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario, DNI o contraseña incorrectos"
        )
    return resultado
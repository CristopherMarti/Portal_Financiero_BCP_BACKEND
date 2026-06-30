# services/auth_service.py
import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from repositories.auth_repository import AuthRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY", "bcp_core_secreto_super_seguro_2026")
ALGORITHM  = os.getenv("ALGORITHM", "HS256")
EXPIRE_MIN = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 120))

class AuthService:
    def __init__(self, db: Session):
        self.repo = AuthRepository(db)

    def autenticar_usuario(self, username: str, dni: str, password: str) -> dict:
        usuario = self.repo.buscar_por_username_y_dni(username, dni)
        if not usuario:
            return None

        if not pwd_context.verify(password, usuario.password_hash):
            self.repo.incrementar_intentos(usuario)
            return None

        self.repo.resetear_intentos(usuario)
        cliente = self.repo.buscar_cliente_por_id(usuario.cliente_id)

        token = self._crear_token({
            "sub":        usuario.username,
            "cliente_id": usuario.cliente_id,
            "nombres":    cliente.nombres if cliente else "",
        })

        return {
            "success":      True,
            "access_token": token,
            "token_type":   "bearer",
            "user_id":      usuario.cliente_id,
            "username":     usuario.username,
            "nombre":       cliente.nombres if cliente else "",
        }

    def _crear_token(self, data: dict) -> str:
        payload = data.copy()
        payload["exp"] = datetime.utcnow() + timedelta(minutes=EXPIRE_MIN)
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
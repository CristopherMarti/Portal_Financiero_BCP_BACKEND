# repositories/auth_repository.py
from sqlalchemy.orm import Session
from models.usuario_hb import UsuarioHomebanking
from models.cliente import Cliente

class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_por_username_y_dni(self, username: str, dni: str):
        """
        Busca al usuario homebanking por username (codcliente)
        y verifica que el DNI coincida con el cliente asociado.
        """
        return (
            self.db.query(UsuarioHomebanking)
            .join(Cliente, UsuarioHomebanking.cliente_id == Cliente.id_cliente)
            .filter(UsuarioHomebanking.username == username)
            .filter(Cliente.dni == dni)
            .filter(UsuarioHomebanking.activo == 'S')
            .filter(UsuarioHomebanking.bloqueado == 'N')
            .first()
        )

    def buscar_cliente_por_id(self, cliente_id: int):
        """Obtiene los datos del cliente por su ID."""
        return self.db.query(Cliente).filter(Cliente.id_cliente == cliente_id).first()

    def incrementar_intentos(self, usuario: UsuarioHomebanking):
        """Incrementa intentos fallidos y bloquea si llega a 3."""
        usuario.intentos_fallidos += 1
        if usuario.intentos_fallidos >= 3:
            usuario.bloqueado = 'S'
        self.db.commit()

    def resetear_intentos(self, usuario: UsuarioHomebanking):
        """Resetea intentos fallidos tras login exitoso."""
        usuario.intentos_fallidos = 0
        self.db.commit()
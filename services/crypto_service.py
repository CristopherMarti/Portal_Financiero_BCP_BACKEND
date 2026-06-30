# services/crypto_service.py
import os
from cryptography.fernet import Fernet

CLAVE_SECRET = os.getenv("CLAVE_CIFRADO")

# Validamos que exista y que tenga el tamaño correcto de Fernet (44 caracteres en base64)
if not CLAVE_SECRET or len(CLAVE_SECRET) != 44:
    # Si es inválida o no existe, genera una segura temporal para que el servidor no muera
    CLAVE_SECRET = Fernet.generate_key().decode()

try:
    fernet = Fernet(CLAVE_SECRET.encode())
except Exception:
    # Segundo respaldo por si falla la inicialización
    fernet = Fernet(Fernet.generate_key())
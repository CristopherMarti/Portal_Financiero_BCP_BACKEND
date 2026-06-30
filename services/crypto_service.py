# services/crypto_service.py
import os
from cryptography.fernet import Fernet

# La clave se obtiene de una variable de entorno, NUNCA del código
CLAVE_SECRET = os.getenv("CLAVE_CIFRADO")

if not CLAVE_SECRET:
    # Genera una clave aleatoria temporal de prueba para entorno de desarrollo local
    CLAVE_SECRET = Fernet.generate_key().decode()

fernet = Fernet(CLAVE_SECRET.encode())

def cifrar_dato(texto: str) -> str:
    """Recibe un texto plano (como el DNI) y lo devuelve encriptado en AES"""
    if not texto:
        return texto
    return fernet.encrypt(texto.encode()).decode()

def descifrar_dato(texto_cifrado: str) -> str:
    """Recibe la cadena encriptada de la BD y la devuelve legible"""
    if not texto_cifrado:
        return texto_cifrado
    return fernet.decrypt(texto_cifrado.encode()).decode()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. Importar esto
from database import engine, Base
from routers import prestamos
from models import cliente, usuario_hb  # agregar esta línea
from routers import prestamos, auth, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. AGREGAR ESTO PARA DAR PERMISO A REACT
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que cualquier frontend se conecte
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prestamos.router, prefix="/api/prestamos", tags=["Préstamos"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(dashboard.router, prefix="/api/cuentas", tags=["Dashboard"])
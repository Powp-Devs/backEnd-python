from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

#Importar os routers
from app.modules.clients.router import router as clients_router
from app.modules.supplier.router import router as supplier_router
from app.modules.employee.router import router as employee_router
from app.modules.setor.router import router as sector_router
from app.modules.products.router import router as products_router

#Importar o motor do banco
from app.core.database import engine, Base

#Importar as models 
from app.modules.clients import models as clients_models
from app.modules.util import models as util_models
from app.modules.supplier import models as supplier_models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API do Powp - System Enterprise",
    description="API para o sistema erp POWP",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers com prefixo /api
app.include_router(clients_router, prefix="/api")
app.include_router(supplier_router, prefix="/api")
app.include_router(employee_router, prefix="/api")
app.include_router(sector_router, prefix="/api")
app.include_router(products_router, prefix="/api")

@app.get("/")
def health_check():
    return{"status": "API online"}
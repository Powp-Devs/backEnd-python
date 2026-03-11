from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.modules.clients.router import router as clients_router

app = FastAPI(
    title="API do Powp - System Enterprise",
    description="API para o sistema ERP voltado ao projeto final de curso",
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

@app.get("/")
def health_check():
    return{"status": "API online"}
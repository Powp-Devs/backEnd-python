from fastapi import FastAPI 
from app.modules.clients.router import router as clients_router

app = FastAPI(
    title="API do Powp - System Enterprise",
    description="API para o sistema ERP voltado ao projeto final de curso",
    version="1.0.0"
)

app.include_router(clients_router)

@app.get("/")
def health_check():
    return{"status": "API online"}
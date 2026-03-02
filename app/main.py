from fastapi import FastAPI 

app = FastAPI(
    title="API do Powp - System Enterprise",
    description="API para o sistema ERP voltado ao projeto final de curso",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return{"status": "API online"}
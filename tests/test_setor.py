from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool 

from app.main import app
from app.core.database import get_db, Base
from app.modules.setor import models

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool 
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_setor():
    dados_new = {
        "setor": "Tecnologia Teste",
        "status": "A"
    }

    response = client.post('/api/setor/cadastrar', json=dados_new)

    assert response.status_code == 201

    json_response = response.json()
    assert json_response["message"] == "Setor cadastrado com sucesso"
    assert json_response["data"]["setor"] == "Tecnologia Teste"
    assert json_response["data"]["status"] == "A"
    assert "codsetor" in json_response["data"]
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
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

def test_criar_fornecedor():
    
    dados_new = {
        "fornecedor": "Fornecedor Teste Aut",
        "fantasia": "Teste Companhia do café",
        "cnpj": "12345678901234",
        "inscricaoestadual": "1425361",
        "tipopessoa": "J",
        "dtcadastro": "2026-04-01",
        "obs": "Teste vindo de uma pipeline",
        "bloqueio": "N",
        "motivo_bloqueio": "",
        "dtbloqueio": "",
        "nome_representante": "Mr. Café",
        "cpf_representante": "12345678969",
        "cep": "75000000",
        "logradouro": "Avenida dos cafés",
        "numero": "8",
        "bairro": "Cappuccino",
        "cidade": "Cafelandia",
        "uf": "GO",
        "pais": "BR",
        "telefone": "40028922",
        "celular": "914145836",
        "email": "cafe@example.com",
        "email2": "cafe2@example.com"
    }
    
    response = client.post('/api/fornecedor/cadastrar', json=dados_new)
    
    assert response.status_code == 201
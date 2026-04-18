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

def test_create_product():

    dados_new = {
        "produto": "Produto de Teste",
        "sku": "Prod. Test",
        "embalagem": "UN",
        "unidade": "CX",
        "gtin": "12",
        "ean": "16516151531",
        "status": "A",
        "obs": "Teste da pipeline",
        "codfornecedor": 1,
        "custo": 50,
        "preco_venda": 10,
        "margem": 4
    }

    response = client.post('api/produtos/cadastrar', json=dados_new)

    assert response.status_code == 201
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Vendas": 3}


def test_post_venda():
    response = client.post(
        "/vendas/",
        json={"nome": "Venda 4", "valor": 400.0, "unidades": 4},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 4,
        "nome": "Venda 4",
        "valor": 400.0,
        "unidades": 4,
    }

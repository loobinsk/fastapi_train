import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_capex():
    data = {
        "project_id": 1,
        "date": "2023-10-03",
        "name": "Тестовый капекс",
        "amount": 1000.0,
        "vat_rate": 0.2,
        "depreciation_period": 5,
        "is_leasing": False,
        "description": "Тестовое описание"
    }
    response = client.post("/capex/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Тестовый капекс"

def test_read_capexs():
    response = client.get("/capex/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_capex_by_id():
    response = client.get("/capex/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_capex():
    data = {
        "name": "Обновленный капекс"
    }
    response = client.patch("/capex/1", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Обновленный капекс"

def test_put_capex():
    data = {
        "name": "Замененный капекс"
    }
    response = client.put("/capex/1", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Замененный капекс"

def test_delete_capex():
    response = client.delete("/capex/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Замененный капекс"

def test_copy_capex():
    response = client.post("/capex/copy/2")  
    assert response.status_code == 200
    assert response.json()["name"] == "Копия капекса"

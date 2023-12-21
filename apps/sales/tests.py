import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Тесты для модели Expense
def test_create_expense():
    data = {
        "project_id": 1,
        "date": "2023-10-03",
        "name": "Тестовый расход",
        "classification": "Классификация",
        "activity_classification": "Классификация деятельности",
        "amount": 1000.0,
        "vat_rate": 0.2,
        "description": "Тестовое описание"
    }
    response = client.post("/expense/", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Тестовый расход"

# Тесты для эндпоинта получения всех расходов
def test_read_expenses():
    response = client.get("/expense/")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Тесты для эндпоинта получения расхода по ID
def test_read_expense_by_id():
    response = client.get("/expense/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

# Тесты для эндпоинта обновления расхода через PATCH
def test_update_expense():
    data = {
        "name": "Обновленный расход"
    }
    response = client.patch("/expense/1", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Обновленный расход"

# Тесты для эндпоинта обновления расхода через PUT
def test_put_expense():
    data = {
        "name": "Замененный расход"
    }
    response = client.put("/expense/1", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Замененный расход"

# Тесты для эндпоинта удаления расхода
def test_delete_expense():
    response = client.delete("/expense/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Замененный расход"

# Тесты для эндпоинта копирования расхода
def test_copy_expense():
    response = client.post("/expense/copy/2")  # Предположим, что есть расход с ID=2
    assert response.status_code == 200
    assert response.json()["name"] == "Копия расхода"
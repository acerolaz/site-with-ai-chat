from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_recipes_seeded() -> None:
    response = client.get("/recipes")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2


def test_create_and_delete_recipe() -> None:
    create = client.post("/recipes", json={"name": "Test", "ingredients": ["a", "b"]})
    assert create.status_code == 201
    recipe_id = create.json()["id"]

    fetched = client.get(f"/recipes/{recipe_id}")
    assert fetched.status_code == 200

    deleted = client.delete(f"/recipes/{recipe_id}")
    assert deleted.status_code == 204

    not_found = client.get(f"/recipes/{recipe_id}")
    assert not_found.status_code == 404


def test_chat_stub_responds() -> None:
    response = client.post("/chat", json={"message": "Bonjour"})
    assert response.status_code == 200
    assert len(response.json()["reply"]) > 0

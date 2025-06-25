import pytest
from app.models.character import Character

@pytest.fixture
def character_data():
    return {
        "name": "TestHero",
        "character_class": "Alchemist",
        "stats": {"hp": 10, "damage": 2, "defense": 1, "speed": 3},
        "abilities": ["Potion Mastery", "Transmute"]
    }

def test_create_character(client, character_data):
    response = client.post("/api/v1/characters/", json=character_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == character_data["name"]
    assert data["character_class"] == character_data["character_class"]
    assert "id" in data

def test_list_characters(client):
    response = client.get("/api/v1/characters/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_character(client, character_data):
    create_resp = client.post("/api/v1/characters/", json=character_data)
    char_id = create_resp.json()["id"]
    response = client.get(f"/api/v1/characters/{char_id}")
    assert response.status_code == 200
    assert response.json()["id"] == char_id

def test_update_character(client, character_data):
    create_resp = client.post("/api/v1/characters/", json=character_data)
    char_id = create_resp.json()["id"]
    update_data = character_data.copy()
    update_data["name"] = "UpdatedHero"
    response = client.put(f"/api/v1/characters/{char_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedHero"

def test_delete_character(client, character_data):
    create_resp = client.post("/api/v1/characters/", json=character_data)
    char_id = create_resp.json()["id"]
    response = client.delete(f"/api/v1/characters/{char_id}")
    assert response.status_code == 200
    assert response.json()["ok"] is True

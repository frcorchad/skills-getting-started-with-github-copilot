from fastapi.testclient import TestClient
import pytest

# Arrange: usar el fixture client de conftest.py
def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "juan.perez@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity}" in response.json()["message"]

def test_signup_duplicate(client):
    # Arrange
    activity = "Chess Club"
    email = "ana.gomez@mergington.edu"
    client.post(f"/activities/{activity}/signup", params={"email": email})  # Primera inscripción

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]

def test_signup_activity_not_found(client):
    # Arrange
    activity = "NoExiste"
    email = "pedro@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

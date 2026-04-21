from fastapi.testclient import TestClient
import pytest

# Arrange: usar el fixture client de conftest.py
def test_get_activities_returns_all(client):
    # Arrange
    # (Nada que preparar, la BD ya tiene datos por defecto)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) >= 1  # Debe haber actividades precargadas
    # Comprobar que cada valor tiene las claves esperadas
    for act in data.values():
        assert "description" in act
        assert "participants" in act

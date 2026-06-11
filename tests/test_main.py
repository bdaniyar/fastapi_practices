"""Tests for the main application."""
import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_hello_index():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


def test_list_items():
    """Test the list items endpoint."""
    response = client.get("/items")
    assert response.status_code == 200
    assert "items" in response.json()


def test_get_item():
    """Test the get item endpoint."""
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["item_id"] == 1

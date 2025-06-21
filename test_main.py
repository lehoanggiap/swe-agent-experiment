import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Calculator API"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_addition():
    response = client.post("/calculate", json={
        "a": 5,
        "b": 3,
        "operation": "add"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_division():
    response = client.post("/calculate", json={
        "a": 10,
        "b": 2,
        "operation": "divide"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_division_by_zero():
    """
    This test WILL FAIL because of the division by zero bug in main.py
    SWE Agent should detect this failure and fix the underlying issue
    """
    response = client.post("/calculate", json={
        "a": 10,
        "b": 0,
        "operation": "divide"
    })
    # This should return a 400 error with proper error message
    # instead of crashing with 500 internal server error
    assert response.status_code == 400
    assert "division by zero" in response.json()["detail"].lower()

def test_subtraction():
    response = client.post("/calculate", json={
        "a": 10,
        "b": 3,
        "operation": "subtract"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 7

def test_multiplication():
    response = client.post("/calculate", json={
        "a": 4,
        "b": 5,
        "operation": "multiply"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 20

def test_invalid_operation():
    response = client.post("/calculate", json={
        "a": 5,
        "b": 3,
        "operation": "power"
    })
    assert response.status_code == 400
    assert "Unsupported operation" in response.json()["detail"]

def test_history():
    # Clear history first
    client.get("/history/clear")
    
    # Make a calculation
    client.post("/calculate", json={
        "a": 2,
        "b": 3,
        "operation": "add"
    })
    
    # Check history
    response = client.get("/history")
    assert response.status_code == 200
    history = response.json()["history"]
    assert len(history) == 1
    assert history[0]["result"] == 5

def test_clear_history():
    # Make a calculation
    client.post("/calculate", json={
        "a": 1,
        "b": 1,
        "operation": "add"
    })
    
    # Clear history
    response = client.get("/history/clear")
    assert response.status_code == 200
    assert "History cleared" in response.json()["message"]
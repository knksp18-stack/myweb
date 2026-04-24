from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello():
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "API Works!"}

def test_grade_A():
    res = client.get("/api/grade?score=90")
    assert res.status_code == 200
    assert res.json()["grade"] == "A"

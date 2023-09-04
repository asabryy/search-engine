from fastapi.testclient import TestClient

from searchEngineApi import app

client = TestClient(app)


def test_query():
    response = client.get("/query")
    assert response.status_code == 200
    assert response.json() == {"Messasge": "I'm querying"}


def test_ingest():
    response = client.post("/ingest")
    assert response.status_code == 200
    assert response.json() == {"Message": "I'm ingesting ..."}

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_lista_todas():
    r = client.get("/opportunities")
    assert r.status_code == 200
    assert len(r.json()) == 4


def test_filtra_por_tipo():
    r = client.get("/opportunities", params={"type": "estagio"})
    assert [o["id"] for o in r.json()] == ["2"]


def test_busca_por_texto():
    r = client.get("/opportunities", params={"q": "hackathon"})
    assert len(r.json()) == 1
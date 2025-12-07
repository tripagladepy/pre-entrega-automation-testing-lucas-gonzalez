import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_by_id():
    """
    Test GET /posts/1
    Valida:
      - Status code 200
      - El JSON contiene un id correcto
      - El body tiene claves esperadas
    """
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200, "El GET no devolvió 200"

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_create_post():
    """
    Test POST /posts
    Valida:
      - Status code 201
      - El JSON retorna los campos enviados
      - Se genera un id (JSONPlaceholder siempre retorna id=101)
    """
    payload = {
        "title": "Tripa QA Automation",
        "body": "Probando POST para el proyecto final",
        "userId": 7
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201, "POST no devolvió 201"

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data  # JSONPlaceholder siempre devuelve id=101


def test_delete_post():
    """
    Test DELETE /posts/1
    Valida:
      - Status code 200 o 204 (depende de la ruta)
      - El body está vacío
    """
    response = requests.delete(f"{BASE_URL}/posts/1")

    # JSONPlaceholder puede devolver 200 o 204 según el servidor
    assert response.status_code in (200, 204), "DELETE no retornó 200/204"

    # El body debe estar vacío
    assert response.text == "" or response.text == "{}"

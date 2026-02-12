import requests

BASE_URL = "https://petstore.swagger.io/v2/swagger.json"


def test_api_response():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")


def test_swagger_ui(page):
    page.goto("https://petstore.swagger.io/")
    page.wait_for_load_state("networkidle")

    assert "Swagger" in page.title()


def test_petstore_api():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

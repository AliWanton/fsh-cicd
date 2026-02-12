import requests

base_url = "https://petstore.swagger.io/v2"
def test_api_response():
    response = requests.get(base_url)
    assert response.status_code == 200
    data = response.json()
    assert "current_user_url" in data


def test_github_ui(page):
    page.goto(base_url)
    page.wait_for_load_state("networkidle")
    assert "Swagger" in page.title()


def test_github_api():
    response = requests.get(base_url)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")


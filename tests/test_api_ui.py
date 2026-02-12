import requests


def test_api_response():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
    data = response.json()
    assert "current_user_url" in data

def test_github_ui(page):
    page.goto("https://github.com")
    page.wait_for_load_state("networkidle")
    assert "GitHub" in page.title()

def test_github_api():
    response = requests.get("https://api.github.com")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

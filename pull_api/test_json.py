import pytest
import json
import requests


# POSITIVE CASES

@pytest.fixture
def session():
    s = requests.Session()
    yield s
    s.close()


def test_get():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    assert response.json()["total"] == 12
    json_data = json.loads(response.text)
    print(json_data)


def test_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"


def test_create():
    payload = {
        "username": "sber_test",
        "responsibilities": "soft_skills"
    }
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code == 201
    assert response.json()["username"] == "sber_test"
    json_data = json.loads(response.text)
    print(json_data)


# NEGATIVE CASES

def test_get_single_user_404():
    response = requests.get("https://reqres.in/api/users/23")
    assert response.status_code == 404
    assert response.json()["error"] == "Not Found"


def test_create_invalid_payload():
    payload = {
        "nick": "not_sber_employee"
    }
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code == 404
    assert response.json()['error'], "Missed work_place"


def test_unauthorized_user():
    payload = {
        "user": "bugbuster",
        "job_title": "software tester"
    }
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code == 404
    assert response.json()['error'], "Unauthorized user"


# Вторая таска

def test_api_homepage():
    response = requests.get("https://reqres.in/api/")
    assert response.status_code == 200
    assert response.json()["url"] == "https://reqres.in/api/"


def test_web_homepage():
    response = requests.get("https://reqres.in/")
    assert response.status_code == 200
    assert response.url == "https://reqres.in/"
    # Дополнительная проверка, что результаты запроса совпадают
    assert response.content == requests.get("https://reqres.in/api/").content


# Третья Таска

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_api_user(session, user_id):
    response = session.get(f"https://reqres.in/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id

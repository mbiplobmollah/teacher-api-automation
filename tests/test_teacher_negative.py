import requests
import os
from dotenv import load_dotenv
from utils.auth import get_headers
from utils.payloads import invalid_teacher_payload

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_create_teacher_invalid_payload():

    print("\n========== INVALID PAYLOAD TEST ==========")

    payload = invalid_teacher_payload()

    response = requests.post(
        f"{BASE_URL}/api/teacher",
        json=payload,
        headers=get_headers()
    )

    print("\nResponse:")
    print(response.json())

    assert response.status_code == 400


def test_get_invalid_teacher():

    print("\n========== INVALID TEACHER TEST ==========")

    response = requests.get(
        f"{BASE_URL}/api/teacher/999999",
        headers=get_headers()
    )

    print("\nResponse:")
    print(response.json())

    assert response.status_code == 404


def test_update_invalid_teacher():

    print("\n========== UPDATE INVALID TEACHER TEST ==========")

    payload = {
        "name": "Test"
    }

    response = requests.put(
        f"{BASE_URL}/api/teacher/999999",
        json=payload,
        headers=get_headers()
    )

    print("\nResponse:")
    print(response.json())

    assert response.status_code == 404


def test_delete_invalid_teacher():

    print("\n========== DELETE INVALID TEACHER TEST ==========")

    response = requests.delete(
        f"{BASE_URL}/api/teacher/999999",
        headers=get_headers()
    )

    print("\nResponse:")
    print(response.json())

    assert response.status_code == 404


def test_create_teacher_without_name():

    print("\n========== CREATE TEACHER WITHOUT NAME ==========")

    payload = {
        "name": "",
        "email": "test@gmail.com",
        "department": "CSE",
        "teacherId": 11111,
        "designation": "Professor"
    }

    response = requests.post(
        f"{BASE_URL}/api/teacher",
        json=payload,
        headers=get_headers()
    )

    print("\nResponse:")
    print(response.json())

    assert response.status_code == 400
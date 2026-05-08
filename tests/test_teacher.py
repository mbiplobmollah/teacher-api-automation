import requests
import os
from dotenv import load_dotenv
from utils.auth import get_headers
from faker import Faker

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_create_teacher(teacher_payload):

    print("\n========== CREATE TEACHER TEST ==========")

    response = requests.post(
        f"{BASE_URL}/api/teacher",
        json=teacher_payload,
        headers=get_headers()
    )

    print("\nCreate Teacher Response:")
    print(response.json())

    assert response.status_code == 201


def test_get_all_teachers():

    print("\n========== GET ALL TEACHERS TEST ==========")

    response = requests.get(
        f"{BASE_URL}/api/teacher",
        headers=get_headers()
    )

    print("\nAll Teachers:")
    print(response.json())

    assert response.status_code == 200


def test_get_teacher_by_id(teacher_payload):

    print("\n========== GET TEACHER BY ID TEST ==========")

    create_response = requests.post(
        f"{BASE_URL}/api/teacher",
        json=teacher_payload,
        headers=get_headers()
    )

    teacher_id = create_response.json()["teacherId"]

    response = requests.get(
        f"{BASE_URL}/api/teacher/{teacher_id}",
        headers=get_headers()
    )

    print("\nTeacher Details:")
    print(response.json())

    assert response.status_code == 200

fake = Faker()

def test_update_teacher(teacher_payload):

    print("\n========== UPDATE TEACHER TEST ==========")

    create_response = requests.post(
        f"{BASE_URL}/api/teacher",
        json=teacher_payload,
        headers=get_headers()
    )

    print("\nCreate Response:")
    print(create_response.json())

    teacher_id = create_response.json()["teacherId"]

    updated_payload = {
        "name": "Updated Teacher",
        "email": fake.email(),
        "department": "MBA",
        "designation": "Lecturer"
    }

    print("\nUpdated Payload:")
    print(updated_payload)

    response = requests.put(
        f"{BASE_URL}/api/teacher/{teacher_id}",
        json=updated_payload,
        headers=get_headers()
    )

    print("\nUpdated Teacher:")
    print(response.json())

    assert response.status_code == 200

def test_delete_teacher(teacher_payload):

    print("\n========== DELETE TEACHER TEST ==========")

    create_response = requests.post(
        f"{BASE_URL}/api/teacher",
        json=teacher_payload,
        headers=get_headers()
    )

    teacher_id = create_response.json()["teacherId"]

    response = requests.delete(
        f"{BASE_URL}/api/teacher/{teacher_id}",
        headers=get_headers()
    )

    print("\nDelete Response:")
    print(response.json())

    assert response.status_code == 200
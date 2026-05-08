import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")


def get_headers():

    print("\nGetting Authentication Token...")

    login_payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=login_payload
    )

    print("Login Status Code:", response.status_code)
    print("Login Response:", response.text)

    token = response.json()["authToken"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    return headers
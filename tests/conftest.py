import pytest
from faker import Faker
import random

fake = Faker()


@pytest.fixture
def teacher_payload():

    payload = {
        "name": fake.name(),
        "email": fake.unique.email(),
        "department": "CSE",
        "teacherId": random.randint(10000, 99999),
        "designation": "Professor"
    }

    print("\nGenerated Teacher Payload:")
    print(payload)

    return payload
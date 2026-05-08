from faker import Faker
import random

fake = Faker()


def invalid_teacher_payload():

    payload = {
        "name": "",
        "email": "wrong-email",
        "department": "",
        "teacherId": "",
        "designation": ""
    }

    print("\nGenerated Invalid Payload:")
    print(payload)

    return payload
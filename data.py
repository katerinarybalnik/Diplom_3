import time
import requests
from faker import Faker

from urls import CREATE_USER_URL


fake = Faker()

def create_user():
    user_data = {
        "email": f"user{time.time_ns()}@example.com",
        "password": "fake1004",
        "name": fake.first_name()
    }

    response = requests.post(CREATE_USER_URL, json=user_data)

    assert response.status_code == 200

    return user_data
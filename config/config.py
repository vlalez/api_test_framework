import os

ENVIRONMENTS = {
    "dev": "https://jsonplaceholder.typicode.com",
    "test": "https://jsonplaceholder.typicode.com",
    "prod": "https://jsonplaceholder.typicode.com"
}

TEST_ENV = os.getenv("TEST_ENV","test")
base_url = ENVIRONMENTS[TEST_ENV]

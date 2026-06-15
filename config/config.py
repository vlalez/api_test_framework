import os

ENVIRONMENTS = {
    "dev": "https://jsonplaceholder.typicode.com",
    "test": "https://jsonplaceholder.typicode.com",
    "prod": "https://jsonplaceholder.typicode.com"
}


def get_base_url() -> str:
    env = os.getenv("TEST_ENV", "test")
    if env not in ENVIRONMENTS:
        raise ValueError(f"Unknown TEST_ENV '{env}'. Valid values: {list(ENVIRONMENTS)}")
    return ENVIRONMENTS[env]

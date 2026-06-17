import requests
from config.config import base_url


def get(endpoint: str) -> requests.Response:
    return requests.get(f'{base_url}{endpoint}')


def post(endpoint: str, payload: dict) -> requests.Response:
    return requests.post(f'{base_url}{endpoint}', json=payload)


def delete(endpoint: str) -> requests.Response:
    return requests.delete(f'{base_url}{endpoint}')


def put(endpoint: str, payload: dict) -> requests.Response:
    return requests.put(f'{base_url}{endpoint}', json=payload)

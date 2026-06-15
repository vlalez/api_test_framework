import requests
from config.config import get_base_url


def get(endpoint: str) -> requests.Response:
    return requests.get(f'{get_base_url()}{endpoint}')


def post(endpoint: str, payload: dict) -> requests.Response:
    return requests.post(f'{get_base_url()}{endpoint}', json=payload)


def delete(endpoint: str) -> requests.Response:
    return requests.delete(f'{get_base_url()}{endpoint}')


def put(endpoint: str, payload: dict) -> requests.Response:
    return requests.put(f'{get_base_url()}{endpoint}', json=payload)

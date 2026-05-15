import requests
from config.config import base_url

#Base URL
#base_url = 'https://jsonplaceholder.typicode.com'

#GET method
def get(endpoint:str)->list:
    '''Send GET request to API endpoint'''
    return requests.get(f'{base_url}{endpoint}')

#POST method
def post(endpoint:str,payload:dict)->None:
    '''Send POST request to API enpont with payload'''
    return requests.post(f'{base_url}{endpoint}', json=payload)

#DELETE method
def delete(endpoint:str)->None:
    '''Send DELETE request to API enpont with payload'''
    return requests.delete(f"{base_url}{endpoint}")

#PUT method
def put(endpoint, payload:str)->None:
    '''Send PUT request to API enpont with payload'''
    return requests.put(f'{base_url}{endpoint}',json=payload)

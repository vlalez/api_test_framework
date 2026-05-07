import requests

#Base URL
base_url = 'https://jsonplaceholder.typicode.com'

#GET method
def get(endpoint)->list:
    '''Send GET request to API endpoint'''
    return requests.get(f'{base_url}{endpoint}')

#POST method
def post(endpoint,payload)->None:
    '''Send POST request to API enpont with payload'''
    return requests.post(f'{base_url}{endpoint}', json=payload)

#DELETE method
def delete(endpoint):
    '''Send DELETE request to API enpont with payload'''
    return requests.delete(f"{base_url}{endpoint}")
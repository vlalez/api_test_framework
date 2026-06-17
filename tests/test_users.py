import os
import pytest
import json
from pathlib import Path

from jsonschema.exceptions import ValidationError
from utils.api_client import get,post,delete,put
from jsonschema import validate
from schemas.user_schema import user_schema
from config.config import TEST_ENV

#Check the environment
def test_environment():
    assert TEST_ENV == 'test'

#Server is up and running
def test_get_user_status_code():
    response = get('/users')
    print( f'Respond from server is:{response.status_code}')
    assert response.status_code ==200

#Response for users request is JSON and is not empty
def test_get_users_response_structure():
    response = get('/users')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
#First user has id, name and email fields
    first_user = data[0]
    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user

#A single user has attributes id==1, name and email
def test_get_single_user():
    response = get('/users/1')
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=user_schema)

#Create a new user using POST request:
def test_create_user():
    payload = {
        "name": "John Tester",
        "email": "john@test.com"
    }
    response = post('/users',payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload['name']
    assert data["email"] == payload['email']

#Delete user with id=1
def test_delete_user():
    response = delete('/users/1')
    assert response.status_code == 200

#Negative test: request a non-existing user
def test_get_non_existing_user():
    response = get('/users/9999')
    assert response.status_code == 404

#Negative test: Check that invalid data is not matching JSON schema
def test_invalid_schema():
    invalid_data = {
        "identififier" : 1
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_data, schema=user_schema)

#Reading JSON file:
def load_test_data():
    path = Path(__file__).parent.parent / "data" / "users.json"
    with open(path) as my_file:
        return json.load(my_file)

#Parameterized request:
@pytest.mark.parametrize('user_data',load_test_data())
def test_get_multiple_users(user_data):
    response = get(f'/users/{user_data['id']}')
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_data['id']
    assert "email" in data

#Update existing user
def test_update_user():
    payload = {
        'id':1,
        "name": "Updated user",
        "email": "updated@test.com"
    }
    response = put('/users/1',payload)
    assert response.status_code == 200
    data = response.json()
    print (data)
    assert data["name"] == payload['name']
    assert data["email"] == payload['email']







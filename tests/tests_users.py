import requests

base_url = 'https://jsonplaceholder.typicode.com'

def test_get_user_status_code():
    response = requests.get(f'{base_url}/users')

    assert response.status_code ==200

def test_get_users_response_structure():
    response = requests.get(f'{base_url}/users')

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_user = data[0]

    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user



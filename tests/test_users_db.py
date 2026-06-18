import pytest
from utils.api_client import get
from utils.db_client import fetch_all_users, fetch_users_with_companies, fetch_user_by_id


# Verify the DB was seeded before running any other DB tests
def test_db_is_seeded():
    users = fetch_all_users()
    assert len(users) > 0, "Database is empty — delete data/test_data.db and re-run to re-seed"


# Every user row in DB must return HTTP 200 from the API
@pytest.mark.parametrize("user", fetch_all_users())
def test_api_returns_200_for_db_user(user):
    response = get(f'/users/{user["id"]}')
    assert response.status_code == 200


# API name must match DB name (SELECT on users table)
@pytest.mark.parametrize("user", fetch_all_users())
def test_api_name_matches_db(user):
    response = get(f'/users/{user["id"]}')
    assert response.status_code == 200
    assert response.json()["name"] == user["name"]


# API email must match DB email (SELECT on users table)
@pytest.mark.parametrize("user", fetch_all_users())
def test_api_email_matches_db(user):
    response = get(f'/users/{user["id"]}')
    assert response.status_code == 200
    assert response.json()["email"] == user["email"]


# API company name must match DB company name (SELECT + JOIN users & companies)
@pytest.mark.parametrize("record", fetch_users_with_companies())
def test_api_company_matches_db(record):
    response = get(f'/users/{record["id"]}')
    assert response.status_code == 200
    api_company = response.json().get("company", {}).get("name", "")
    assert api_company == record["company_name"]


# Total user count from JOIN must equal API list length
def test_joined_record_count_matches_api():
    db_records = fetch_users_with_companies()
    api_response = get('/users')
    assert api_response.status_code == 200
    assert len(db_records) == len(api_response.json())


# Fetch a single user via JOIN and cross-check both name and company with API
def test_single_user_join_lookup():
    record = fetch_user_by_id(1)
    assert record is not None
    response = get('/users/1')
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == record["name"]
    assert data["company"]["name"] == record["company_name"]

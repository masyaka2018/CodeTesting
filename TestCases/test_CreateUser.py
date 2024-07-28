import requests
import json
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\CreateUser.json', 'r')
    yield

@pytest.mark.Smoke
def test_create_new_user(start_exec):
    # read Input json file
    json_input = file.read()
    request_json = json.loads(json_input)

    # Make request with Json input body
    response = requests.post(url, request_json)
    assert response.status_code == 201

@pytest.mark.Sanity
def test_create_other_user(start_exec):
    # read Input json file
    json_input = file.read()
    request_json = json.loads(json_input)

    # Make request with Json input body
    response = requests.post(url, request_json)
    assert response.status_code == 201
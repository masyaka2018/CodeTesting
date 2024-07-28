import requests
import json
import jsonpath


def test_with_authentification():
    token_url = "https://thetestingworldapi.com/Token"
    data = {'grand_type': 'token', 'username': 'admin', 'password': 'adminpass'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer' + token_value[0]}
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/1104"
    response = requests.get(API_URL, headers=auth)
    print(response.text)

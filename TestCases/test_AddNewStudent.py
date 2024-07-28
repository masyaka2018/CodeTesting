import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\RequestJson.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_update_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10300233"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\RequestJson.json', 'r')
    json_request = json.loads(file.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10300233"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10300233"
    response = requests.get(API_URL)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 10300233
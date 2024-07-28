import requests
import json
import jsonpath

def test_add_new_student():
    global id
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\AddStudent.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL,json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_details():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)


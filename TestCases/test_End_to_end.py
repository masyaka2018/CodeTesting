import requests
import json
import jsonpath

def test_Add_new_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\RequestJson.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\TechDetails.json', 'r')
    json_request = json.loads(file.read())
    json_request['id'] = int(id[0])
    json_request['st_id'] = id[0]
    response = requests.post(tech_api_url, json_request)
    print(response.text)

    add_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\address.json', 'r')
    json_request = json.loads(file.read())
    json_request['stId'] = id[0]
    response = requests.post(add_api_url, json_request)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/10300233"
    response = requests.get(final_details)
    print(response.text)
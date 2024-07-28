import json
import requests
from DataDriven import Library

def test_add_multiple_students():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\AddNewStudent.json', 'r')
    json_request = json.loads(file.read())

    obj = Library.Common('C:\\Users\\Marina_my_folder\\testing_purpose\\TestData.xlsx', 'Лист1')
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(api_url, updated_json_request)
        print(response.text)
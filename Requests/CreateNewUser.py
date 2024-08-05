import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# read Input json file
file = open('C:\\Users\\Marina_my_folder\\testing_purpose\\AddStudent.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make request with Json input body
response = requests.post(url, request_json)
assert response.status_code == 201

#fetch header from reponse
print(response.headers.get('Content-Length'))

#Parse response to JSON format
response_json = json.loads(response.text)

#Pik id
id = jsonpath.jsonpath(response_json,'id')
print(id[0])
import requests

param = {'name': "testingWorld", 'email': "Trainer: testingworld@gmail.com", 'number': '+38093-102-39-32'}
response = requests.get("https://httpbin.org/get", params=param)
print(response.text)

import requests
from requests.auth import HTTPBasicAuth

def test_with_authentification():
    response = requests.get("https://api.github.com/user",auth=HTTPBasicAuth('masyaka2018', 'Mariwka2013'))
    print(response.text)
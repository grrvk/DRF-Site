import requests

endpoint = "http://localhost:8000/main/"

get_response = requests.post(endpoint, json={'number': 7})
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
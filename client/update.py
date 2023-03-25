import requests

endpoint = "http://localhost:8000/api/transport/1/update/"

data = {
    "number": 577,
}

get_response = requests.put(endpoint, json=data)
# print(get_response.text)
print(get_response.json())
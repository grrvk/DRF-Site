import requests

endpoint = "http://localhost:8000/api/transport/"

data = {
    "number": 225,
    "route": 1,
    "num_of_passengers": 50,
    "type": "Train",
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
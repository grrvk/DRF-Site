import requests

transport_id = input("Write id\n")
try:
    transport_id = int(transport_id)
except:
    transport_id = None
    print(f"{transport_id} is not valid")

if transport_id:
    endpoint = f"http://localhost:8000/api/transport/{transport_id}/delete/"

    get_response = requests.delete(endpoint)
    # print(get_response.text)
    print(get_response.status_code, get_response.status_code==204)
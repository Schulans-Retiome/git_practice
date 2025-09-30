import json
import requests


base_url = "https://reqres.in/api/users"

headers_test = {
    'Content-Type': 'application/json',
    "x-api-key": "reqres-free-v1"
}

# payload = {
#     "name": "Kokey",
#     "job": "alien"
# }

json_file = open('./user_config.json')
json_payload = json.load(json_file)

response = requests.post(url=base_url, headers=headers_test, json=json_payload)
print(response.status_code)
print(response.text)
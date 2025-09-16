import requests


headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
}

request_payload = {
    "id": 250,
    "title": "testing 10",
    "dueDate": "2025-09-16T14:01:33.350Z",
    "completed": True
}

# POST is to create data
response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Activities',
                         headers=headers,
                         json=request_payload)


print(response.status_code)
print(response.json())

data = response.json()

assert response.status_code == 200
assert data['id'] == 250
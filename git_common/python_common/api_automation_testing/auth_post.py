import requests


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 561c643a279ba086ede8a5f1e82ef1f90463f9620a8cb9957cd0b9dcd162a5ee'
}

body = {
    "id": 8137716,
    "name": "deedee",
    "email": "testing.api12345@example.com",
    "gender": "male",
    "status": "active"
}

url = 'https://gorest.co.in/public/v2/users'
response = requests.post(url=url, headers=headers, json=body)

# Prints the response from POST in JSON format
print(response.json())

# Assert if a new resource is created (201)
assert response.status_code == 201

# GET request only on the id
# Converts (typecasting) the id (int) to str
url = url + '/' + str(response.json()['id'])

get_response = requests.get(url=url, headers=headers, json=body)
print(get_response.json())
assert get_response.status_code == 200


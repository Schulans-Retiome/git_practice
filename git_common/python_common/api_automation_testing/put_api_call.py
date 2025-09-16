import requests


head = {
    'Accept': 'text/plain',
}

# PUT is to update
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/13',
                        headers=head)
print('Before update')
print(response.json())

header_put = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
}

put_payload = {
  "id": 15,
  "title": "kev",
  "dueDate": "2025-09-16T14:28:04.587Z",
  "completed": True
}

response_put = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Activities/13',
                            headers=header_put,
                            json=put_payload)

print('After uppdate')
print(response_put.json())
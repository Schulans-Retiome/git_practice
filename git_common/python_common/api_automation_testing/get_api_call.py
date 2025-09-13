import requests

head = {
    'Accept': 'text/plain',
    'id': '3'
}

response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/3', headers=head)

print('----------STATUS CODE----------')
# returns status code
print(response.status_code)

print('----------JSON DATA----------')
# This returns a json
print(response.json())

print('----------TEXT DATA----------')
# text will convert the json to string
print(response.text)

print('----------TESTING----------')
# Testing status code should be successful (200)
expected_status_code = 200
assert response.status_code == expected_status_code, \
    f'Response status code is "{response.status_code}" instead of expected "{expected_status_code}"'

print('----------TESTING SUCCESS----------')


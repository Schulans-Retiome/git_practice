import requests


parameters = {
    'page': 1,
    'per_page': 3
}

url = 'https://gorest.co.in/public/v2/users'

# We passed params argument
response = requests.get(url=url, params=parameters)
print(response.json())
assert response.status_code == 200
# TODO: Learn why headers authorization not required anymore

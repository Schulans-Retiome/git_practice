import requests

class ApiClient:
    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.headers = headers

    def get(self, endpoint=None):
        url = f'{self.api_url}/{endpoint}'
        response = requests.get(url, headers=self.headers)
        return response
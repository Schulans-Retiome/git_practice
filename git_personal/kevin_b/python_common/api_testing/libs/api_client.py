import requests


class ApiClient:
    def __init__(self, base_url, username=None, password=None, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        if token:
            self.session.headers.update({'Authorization': f'Bearer {token}'})

        if username and password:
            self.session.auth = (username, password)

        self.session.headers.update({'Content-Type': 'application/json'})

    def get(self, endpoint, **kwargs):
        return self.session.get(self.base_url + endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.session.post(self.base_url + endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.session.put(self.base_url + endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(self.base_url + endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.session.patch(self.base_url + endpoint, **kwargs)

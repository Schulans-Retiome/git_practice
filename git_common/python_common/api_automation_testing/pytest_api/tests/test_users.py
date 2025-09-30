import pytest
from git_common.python_common.api_automation_testing.pytest_api.utils.api_client import ApiClient

base_url = 'https://jsonplaceholder.typicode.com'
header = {
    'Content-Type': 'application/json',
}

@pytest.fixture(scope='module')
def api_client():
    return ApiClient(base_url, header)

def test_get_users(api_client):
    response = api_client.get("users")
    assert response.status_code == 200
    assert len(response.json()) > 0
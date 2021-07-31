import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_user_list(test_app, requests_mock):
    path_client = "/users"

    url_users_list = USERS_BACKEND_URL + "/users"
    json_users_list = [{"id": 1}, {"id": 2}]
    requests_mock.get(url_users_list, status_code=200, json=json_users_list)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_users_list


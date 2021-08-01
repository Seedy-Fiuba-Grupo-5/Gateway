import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_admins_list(test_app, requests_mock):
    path_client = "/admins"

    url_admins_list = USERS_BACKEND_URL + "/admins"
    json_admins_list = [{"id": 1}, {"id": 2}]
    requests_mock.get(url_admins_list, status_code=200, json=json_admins_list)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_admins_list

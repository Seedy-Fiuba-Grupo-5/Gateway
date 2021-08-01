import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_post_admins_login(test_app, requests_mock):
    path_client = "/admins/login"
    data_client = {"password": "a password"}

    url_admins_list = USERS_BACKEND_URL + "/admins/login"
    json_admin = { "token": "a token" }
    requests_mock.post(url_admins_list, status_code=200, json=json_admin)

    client = test_app.test_client()
    response = client.post(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_admin

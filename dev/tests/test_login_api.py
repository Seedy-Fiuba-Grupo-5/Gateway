import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_post_login(test_app, requests_mock):
    path_client = "/users/login"
    data_client = {}

    url_login = USERS_BACKEND_URL + "/users/login"
    json_login = { "token": "a token" }
    requests_mock.post(url_login, status_code=200, json=json_login)

    client = test_app.test_client()
    response = client.post(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_login



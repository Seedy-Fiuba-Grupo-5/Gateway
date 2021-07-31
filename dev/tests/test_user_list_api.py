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

def test_post_user_list(test_app, requests_mock):
    user_id = 1
    path_client = "/users"
    data_client = {}

    url_user = USERS_BACKEND_URL + "/users"
    json_user = { "id": user_id }
    requests_mock.post(url_user, status_code=201, json=json_user)

    url_pay = PAYMENTS_BACKEND_URL + "/wallets"
    json_pay = {
        "address": "an address",
        "privateKey": "a private key"
    }
    requests_mock.post(url_pay, status_code=201, json=json_pay)

    client = test_app.test_client()
    response = client.post(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 201
    body = json.loads(response.data.decode())
    assert body == {**json_user, **json_pay}


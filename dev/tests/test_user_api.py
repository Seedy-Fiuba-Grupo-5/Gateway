import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_seer(test_app, requests_mock):
    user_id = 1
    token = "aToken"
    path_client = "/users/" + str(user_id) + "?token=" + token

    new_token = "a new token"
    url_user = USERS_BACKEND_URL + "/users/" + str(user_id)
    json_user = { "token": new_token }
    requests_mock.get(url_user, status_code=200, json=json_user)

    url_auth = USERS_BACKEND_URL + "/users/auth"
    json_auth = {}
    requests_mock.post(url_auth, status_code=200, json=json_auth)

    url_pay = PAYMENTS_BACKEND_URL + "/wallets/" + str(user_id)
    json_pay = {
        "address": "an address",
        "privateKey" : "a private key",
        "balance": "a balance"
    }
    requests_mock.get(url_pay, status_code=200, json=json_pay)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == {**json_user, **json_pay}

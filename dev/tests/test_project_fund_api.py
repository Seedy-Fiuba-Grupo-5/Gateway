import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_post_project_funds(test_app, requests_mock):
    project_id = 1

    new_token = "a new token"
    url_auth = USERS_BACKEND_URL + "/users/auth"
    json_auth = {"token": new_token}
    requests_mock.post(url_auth, status_code=200, json=json_auth)

    url_funds = PAYMENTS_BACKEND_URL + "/projects/" + str(project_id) + "/funds"
    requests_mock.post(url_funds, status_code=202, json={})

    client = test_app.test_client()
    path_client = "/projects/" + str(project_id) + "/funds"
    token = "a token"
    user_id = 1
    amount_ethers = 0.01
    data_client = {
        "token": token,
        "userPublicId": user_id,
        "amountEthers": amount_ethers
    }
    response = client.post(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 202
    body = json.loads(response.data.decode())
    assert body['token'] == new_token

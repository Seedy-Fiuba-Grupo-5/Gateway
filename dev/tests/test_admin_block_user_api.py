import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_patch_admin_block_user(test_app, requests_mock):
    user_id = 1
    token = "a token"
    path_client = "/admins/users/" + str(user_id)
    data_client = { "token": token }

    new_token = "a new token"
    url_block_user = USERS_BACKEND_URL + "/admins/users/" + str(user_id)
    json_block_user = { "token": new_token }
    requests_mock.patch(url_block_user, status_code=200, json=json_block_user)

    client = test_app.test_client()
    response = client.patch(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_block_user

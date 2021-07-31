import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_project(test_app, requests_mock):
    project_id = 1
    user_id = 1
    token = "token"
    path_client = "/projects/" + str(project_id) + "?token=" + token
    data_client = {}

    url_project = PROJECTS_BACKEND_URL + "/projects/" + str(project_id)
    json_project = {}
    requests_mock.get(url_project, status_code=200, json=json_project)

    url_user_project = USERS_BACKEND_URL + "/projects/" + str(project_id)
    json_user_project = { "user_id": user_id }
    requests_mock.get(url_user_project, status_code=200, json=json_user_project)

    new_token = "a new token"
    url_user = USERS_BACKEND_URL + "/users/" + str(user_id)
    json_user = { "token": new_token }
    requests_mock.get(url_user, status_code=200, json=json_user)

    url_pay = PAYMENTS_BACKEND_URL + "/projects/" + str(project_id)
    json_pay = {}
    requests_mock.get(url_pay, status_code=200, json=json_pay)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body['user'] == json_user
    assert body['payments'] == json_pay

def test_patch_project(test_app, requests_mock):
    project_id = 1
    user_id = 1
    token = "a token"
    path_client = "/projects/" + str(project_id)
    data_client = { "token": token }

    url_user_project = USERS_BACKEND_URL + "/projects/" + str(project_id)
    json_user_project = { "user_id": user_id }
    requests_mock.get(url_user_project, status_code=200, json=json_user_project)

    url_auth = USERS_BACKEND_URL + "/users/auth"
    json_auth = {}
    requests_mock.post(url_auth, status_code=200, json=json_auth)

    url_project = PROJECTS_BACKEND_URL + "/projects/" + str(project_id)
    json_project = {}
    requests_mock.patch(url_project, status_code=200, json=json_project)

    client = test_app.test_client()
    response = client.patch(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_project


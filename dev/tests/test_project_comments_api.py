import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_comments(test_app, requests_mock):
    project_id = 1
    user_id = 1
    token = "a token"
    path_client = "/commentary/" + str(project_id) + "?token=" + token + "&userId=" + str(user_id)

    url_comment = PROJECTS_BACKEND_URL + "/commentary/" + str(project_id)
    json_comment = {}
    requests_mock.get(url_comment, status_code=200, json=json_comment)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_comment

def test_post_comment(test_app, requests_mock):
    project_id = 1
    path_client = "/commentary/" + str(project_id)
    data_client = {}

    url_comment = PROJECTS_BACKEND_URL + "/commentary/" + str(project_id)
    json_comment = {}
    requests_mock.post(url_comment, status_code=201, json=json_comment)

    client = test_app.test_client()
    response = client.post(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 201
    body = json.loads(response.data.decode())
    assert body == json_comment

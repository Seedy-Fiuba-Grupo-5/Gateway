import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_projects_list(test_app, requests_mock):
    path_client = "/projects?type=someType&name=someName"

    url_project_list = PROJECTS_BACKEND_URL + path_client
    json_project_list = [{"id": 1}, {"id": 2}, {"id": 3}]
    requests_mock.get(url_project_list, status_code=200, json=json_project_list)

    client = test_app.test_client()

    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_project_list

import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_my_projects(test_app, requests_mock):
    user_id = 1
    project_id_1 = 1
    project_id_2 = 2
    url_users = USERS_BACKEND_URL + "/users/" + str(user_id) + "/projects"
    url_project_1 = PROJECTS_BACKEND_URL + "/projects/" + str(project_id_1)
    url_project_2 = PROJECTS_BACKEND_URL + "/projects/" + str(project_id_2)
    json_users = {"project_id": [project_id_1, project_id_2]}
    json_project_1 = {"id": project_id_1}
    json_project_2 = {"id": project_id_2}
    requests_mock.get(url_users, status_code=200, json=json_users)
    requests_mock.get(url_project_1, status_code=200, json=json_project_1)
    requests_mock.get(url_project_2, status_code=200, json=json_project_2)
    client = test_app.test_client()
    path_client = "/users/" + str(user_id) + "/projects"
    data_client = { "token": "a token" }
    response = client.get(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert len(body) == 2


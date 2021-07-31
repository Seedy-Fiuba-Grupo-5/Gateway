import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_favorite_projects(test_app, requests_mock):
    user_id = 1
    project_id_1 = 1
    project_id_2 = 2

    url_fav = USERS_BACKEND_URL + "/users/" + str(user_id) + "/favorites"
    json_fav = { "projects_id": [project_id_1, project_id_2] }
    requests_mock.get(url_fav, status_code=200, json=json_fav)

    url_project_1 = PROJECTS_BACKEND_URL + "/projects/" + str(project_id_1)
    url_project_2 = PROJECTS_BACKEND_URL + "/projects/" + str(project_id_2)
    json_project_1 = {"id": project_id_1}
    json_project_2 = {"id": project_id_2}
    requests_mock.get(url_project_1, status_code=200, json=json_project_1)
    requests_mock.get(url_project_2, status_code=200, json=json_project_2)

    client = test_app.test_client()
    path_client = "/users/" + str(user_id) + "/favorites"
    data_client = {}
    response = client.get(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert len(body) == 2


def test_post_favorite_project(test_app, requests_mock):
    user_id = 1
    project_id = 1
    data_client = { "project_id": project_id }

    url_fav_user = USERS_BACKEND_URL + "/users/" + str(user_id) + "/favorites"
    requests_mock.post(url_fav_user, status_code=201, json=data_client)

    url_fav_proj = PROJECTS_BACKEND_URL + "/projects/" + str(project_id) + "/favorites"
    requests_mock.post(url_fav_proj, status_code=201, json={})

    client = test_app.test_client()
    path_client = "/users/" + str(user_id) + "/favorites"
    response = client.post(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 201

def test_delete_favorite_project(test_app, requests_mock):
    user_id = 1
    project_id = 1
    data_client = { "project_id": project_id }
    response_client = {}
    url_fav_user = USERS_BACKEND_URL + "/users/" + str(user_id) + "/favorites"
    requests_mock.delete(url_fav_user, status_code=200, json=data_client)

    url_fav_proj = PROJECTS_BACKEND_URL + "/projects/" + str(project_id) + "/favorites"
    requests_mock.delete(url_fav_proj, status_code=200, json=response_client)

    client = test_app.test_client()
    path_client = '/users/' + str(user_id) + "/favorites"
    response = client.delete(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 200
    # assert response.body == response_client

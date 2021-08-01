import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_seer(test_app, requests_mock):
    seer_id = 1
    path_client = "/seers/" + str(seer_id)

    url_seer = USERS_BACKEND_URL + "/seers/" + str(seer_id)
    json_seer = { "id": seer_id }
    requests_mock.get(url_seer, status_code=200, json=json_seer)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_seer

def test_post_seer(test_app, requests_mock):
    seer_id = 1
    path_client = "/seers/" + str(seer_id)
    data_client = {}

    url_seer = USERS_BACKEND_URL + "/seers/" + str(seer_id)
    json_seer = { "project_info": "some project info" }
    requests_mock.post(url_seer, status_code=201, json=json_seer)

    client = test_app.test_client()
    response = client.post(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 201
    body = json.loads(response.data.decode())
    assert body == json_seer

def test_patch_seer(test_app, requests_mock):
    seer_id = 1
    project_id = 1
    path_client = "/seers/" + str(seer_id)
    data_client = { "project_id": project_id }

    url_pay = PAYMENTS_BACKEND_URL + "/projects/" + str(project_id)
    json_pay = {}
    requests_mock.patch(url_pay, status_code=202, json=json_pay)

    url_seer = USERS_BACKEND_URL + "/seers/" + str(seer_id)
    json_seer = { "success": "success" }
    requests_mock.patch(url_seer, status_code=200, json=json_seer)

    client = test_app.test_client()
    response = client.patch(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_seer


def test_delete_seer(test_app, requests_mock):
    seer_id = 1
    project_id = 1
    path_client = "/seers/" + str(seer_id)
    data_client = {}

    url_seer = USERS_BACKEND_URL + "/seers/" + str(seer_id)
    json_seer = { "success": "success" }
    requests_mock.delete(url_seer, status_code=200, json=json_seer)

    client = test_app.test_client()
    response = client.delete(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_seer


import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_ratings(test_app, requests_mock):
    project_id = 1
    path_client = "/projects/" + str(project_id) + "/rate"
    data_client = {}
    body_client = {}

    url_rate = PROJECTS_BACKEND_URL + "/projects/" + str(project_id) + "/rate"
    requests_mock.get(url_rate, status_code=200, json=body_client)

    client = test_app.test_client()
    response = client.get(path_client, data=json.dumps(data_client), content_type="application/json")
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == body_client

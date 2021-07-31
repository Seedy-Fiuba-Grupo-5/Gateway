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

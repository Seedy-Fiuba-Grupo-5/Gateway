import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_users_metrics(test_app, requests_mock):
    path_client = "/users/metrics"

    url_metrics = USERS_BACKEND_URL + "/users/metrics"
    json_metrics = {
        'percentage_blocked': 0.5,
        'percentage_with_project': 0.7,
        'percentage_seer': 0.3
    }
    requests_mock.get(url_metrics, status_code=200, json=json_metrics)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_metrics

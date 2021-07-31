import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_projects_metrics(test_app, requests_mock):
    path_client = "/projects/metrics"

    url_metrics = PROJECTS_BACKEND_URL + "/projects/metrics"
    json_metrics = {"most_popular_type": 'Comics',
                    "avg_goal": 0.01,
                    "avg_duration": 5}
    requests_mock.get(url_metrics, status_code=200, json=json_metrics)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_metrics

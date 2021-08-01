import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_admin(test_app, requests_mock):
    admin_id = 1
    path_client = "/admins/" + str(admin_id)

    url_admin = USERS_BACKEND_URL + "/admins/" + str(admin_id)
    json_admin = {}
    requests_mock.get(url_admin, status_code=200, json=json_admin)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_admin

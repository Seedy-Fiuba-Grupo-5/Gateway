import json
import os

PROJECTS_BACKEND_URL = os.getenv('PROJECTS_BACKEND_URL')
USERS_BACKEND_URL = os.getenv('USERS_BACKEND_URL')
PAYMENTS_BACKEND_URL = os.getenv('PAYMENTS_BACKEND_URL')

def test_get_user_messages(test_app, requests_mock):
    user_id = 1
    token = "aToken"
    path_client = "/messages/" + str(user_id) + "?token=" + token

    url_messages = USERS_BACKEND_URL + "/messages/" + str(user_id)
    json_messages = [{"text": "some text"}, {"text": "other text"}]
    requests_mock.get(url_messages, status_code=200, json=json_messages)

    client = test_app.test_client()
    response = client.get(path_client)
    assert response.status_code == 200
    body = json.loads(response.data.decode())
    assert body == json_messages

def test_post_user_message(test_app, requests_mock):
    user_id = 1
    other_id = 2
    path_client = "/messages/" + str(user_id)
    data_client = {}

    url_messages = USERS_BACKEND_URL + "/messages/" + str(user_id)
    json_messages = {"id_1": other_id}
    requests_mock.post(url_messages, status_code=201, json=json_messages)

    client = test_app.test_client()
    response = client.post(path_client, data=json.dumps(data_client), content_type='application/json')
    assert response.status_code == 201
    body = json.loads(response.data.decode())
    assert body == json_messages



import requests

task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://reqres.in/api/users/1', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))
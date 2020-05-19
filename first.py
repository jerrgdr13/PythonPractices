import requests

resp = requests.get('https://reqres.in/api/users/1')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(first_name, last_name))
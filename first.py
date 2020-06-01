import requests

resp = requests.get('https://reqres.in/api/users/2')
print(resp.text)

#if resp.status_code == 200:
    # This means something went wrong.
    #raise ApiError('GET /user/ {}'.format(resp.status_code))
    #print('Success!')
#elif resp.status_code != 200:
#    print('Not Found.')
#for data in resp.json():
#    print('{} {}'.format(first_name, last_name))
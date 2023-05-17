import requests


def api_login():
    payload = {
        'username': '0302226873',
        'password': '0302226873',
    }
    headers = {'Authorization': 'Token 054919424e5f80f83b0a3f91493a641835fdc950'}
    r = requests.post('http://127.0.0.1:8000/api/login/', data=payload, headers=headers)
    if r.status_code == 200:
        items = r.json()
        print(items)
    else:
        print(r.text)


api_login()

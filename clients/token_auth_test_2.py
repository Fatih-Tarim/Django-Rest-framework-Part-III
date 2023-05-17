import requests
from pprint import pprint

# {'key':'9cb38a8ee0d25e1d403d67614b548bbfa85e1d48'}
def client():
    token = 'Token 9cb38a8ee0d25e1d403d67614b548bbfa85e1d48'
    credentials = {
        "username": "fıt",
        "email": "",
        "password": "123"
    }
    headers = {
        'Authorization' : token
    }
    response = requests.get(
        url = 'http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers = headers,
    )
    print('Status Code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()
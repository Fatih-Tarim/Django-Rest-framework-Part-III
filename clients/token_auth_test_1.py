import requests
from pprint import pprint

# {'key':'9cb38a8ee0d25e1d403d67614b548bbfa85e1d48'}
def client():
    credentials = {
        "username": "fıt",
        "email": "",
        "password": "123"
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data = credentials
    )
    print('Status Code: ', response.status_code)

    response_data = response.text
    pprint(response_data)

if __name__ == '__main__':
    client()
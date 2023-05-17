import requests
from pprint import pprint
import datetime

# {'key':'9cb38a8ee0d25e1d403d67614b548bbfa85e1d48'}
def client():
    # now = now()
    credentials = {
        "username": "rest_test_reg",
        "email": "test@gmail.com",
        # "guncellenme_tarihi" : now,
        "password1": "123",
        "password2": "123",
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registiration/',
        data = credentials
    )
    print('Status Code: ', response.status_code)

    response_data = response.text
    pprint(response_data)

if __name__ == '__main__':
    client()
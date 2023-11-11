import random
import string

import pytest
import requests

from tests.config import URL_AUTH, BASE_URL, TEST_USER_NAME, TEST_USER_PASSWORD


@pytest.fixture(scope='session')
def get_new_cookies():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "username": TEST_USER_NAME,
        "password": TEST_USER_PASSWORD
    }
    r = requests.post(f'{BASE_URL}{URL_AUTH}/jwt/login',
                      headers=headers,
                      data=payload)

    return r.cookies.get_dict()

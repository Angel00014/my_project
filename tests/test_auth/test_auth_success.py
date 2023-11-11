import random
import string

import pytest
import requests

from src.auth.schemas import UserRead
from tests.config import URL_AUTH, BASE_URL

email = ''
password = ''
cookies = {}


def test_create_user_success():
    global email
    global password

    email = str(''.join(random.choices(string.ascii_letters, k=8)) + "@mail.ru")
    password = str(''.join(random.choices(string.ascii_letters, k=8)))

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}

    payload = {
        "username": str(''.join(random.choices(string.ascii_letters, k=8))),
        "email": email,
        "password": password,
        "role": 0,
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
    }
    r = requests.post(f'{BASE_URL}{URL_AUTH}/register',
                      headers=headers,
                      json=payload)

    assert r.status_code == 201


def test_login_user_success():
    global cookies

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "username": email,
        "password": password
    }
    r = requests.post(f'{BASE_URL}{URL_AUTH}/jwt/login',
                      headers=headers,
                      data=payload)

    cookies = r.cookies.get_dict()

    assert r.status_code == 204
    assert r.cookies.get_dict()['token'] is not None


def test_logout_user_success():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(f'{BASE_URL}{URL_AUTH}/jwt/logout',
                      headers=headers, cookies=cookies)

    assert r.status_code == 204

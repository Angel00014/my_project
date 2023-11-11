import random
import string

import pytest
import requests

from tests.config import BASE_URL, URL_AUTH, TEST_USER_NAME, TEST_USER_PASSWORD, URL_CATEGORY, URL_RECORD

cookies = {}
id_category = 0
id_record = 0
name_record = ''
url_record = ''


def test_login_user():
    global cookies

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

    cookies = r.cookies.get_dict()

    assert r.status_code == 204
    assert r.cookies.get_dict()['token'] is not None


def test_get_all_category():
    global id_category

    params = {
        'skip': 0,
        'limit': 100
    }

    r = requests.get(f'{BASE_URL}{URL_CATEGORY}',
                     cookies=cookies,
                     params=params)

    for item in r.json():
        if item['status'] == "1":
            id_category = item['id']
            break
        else:
            continue

    assert r.status_code == 200


def test_create_record():
    global id_record
    global name_record
    global url_record

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}

    name_record = ''.join(random.choices(string.ascii_letters, k=8))
    url_record = 'http://' + str(''.join(random.choices(string.ascii_letters, k=8)))

    payload = {
        "name": name_record,
        "url": url_record,
        "category_id": id_category
    }

    r = requests.post(f'{BASE_URL}{URL_RECORD}',
                      headers=headers,
                      json=payload,
                      cookies=cookies)

    id_record = r.json()['id']

    assert r.status_code == 200


def test_get_all_record():
    params = {
        "skip": 0,
        "limit": 100
    }

    r = requests.get(f'{BASE_URL}{URL_RECORD}',
                     params=params,
                     cookies=cookies)

    decision = False
    print(id_record)



    for item in r.json():
        print(item)
        if item['id'] == id_record:
            decision = True
            break
        else:
            continue

    assert r.status_code == 200
    assert decision is True


def test_get_one_record():
    r = requests.get(f'{BASE_URL}{URL_RECORD}/{id_record}',
                     cookies=cookies)

    assert r.status_code == 200
    assert r.json()['name'] == name_record
    assert r.json()['url'] == url_record

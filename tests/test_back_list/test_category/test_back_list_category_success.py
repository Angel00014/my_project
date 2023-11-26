import random
import string

import pytest
import requests

from tests.config import BASE_URL, URL_CATEGORY

id_category = 0
new_name = ''


def test_create_category_success(get_new_cookies):

    global id_category

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}

    payload = {
        "name": str(''.join(random.choices(string.ascii_letters, k=8))),
    }
    r = requests.post(f'{BASE_URL}{URL_CATEGORY}',
                      headers=headers,
                      json=payload,
                      cookies=get_new_cookies)

    id_category = r.json()['id']

    assert r.status_code == 200


def test_update_category_success(get_new_cookies):
    global new_name

    new_name = str(''.join(random.choices(string.ascii_letters, k=8)))

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}

    payload = {
        "name": new_name,
        "id": id_category,
        "status": "0"
    }
    r = requests.patch(f'{BASE_URL}{URL_CATEGORY}',
                       headers=headers,
                       json=payload,
                       cookies=get_new_cookies)

    assert r.status_code == 200
    assert r.json()['name'] == new_name


def test_get_all_category_success(get_new_cookies):
    params = {
        'skip': 0,
        'limit': 100
    }

    r = requests.get(f'{BASE_URL}{URL_CATEGORY}',
                     cookies=get_new_cookies,
                     params=params)
    decision = False

    for item in r.json():
        if item['id'] == id_category:
            decision = True
            break
        else:
            continue

    assert r.status_code == 200
    assert decision is True


def test_get_one_category_success(get_new_cookies):
    params = {
        'skip': 0,
        'limit': 100
    }

    r = requests.get(f'{BASE_URL}{URL_CATEGORY}/{id_category}',
                     cookies=get_new_cookies,
                     params=params)

    assert r.status_code == 200
    assert r.json()['name'] == new_name
    assert r.json()['status'] == "0"

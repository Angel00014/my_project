import logging
import random
import string

import pytest
import requests

from tests.config import BASE_URL, URL_RECORD, URL_CATEGORY

id_record = 0
id_category = 0
id_category_record = 0
new_category_id = 0
new_name_record = ''
new_url_record = ''


def test_get_new_category_before(get_new_cookies):
    global new_category_id
    global id_category

    r = requests.get(f'{BASE_URL}{URL_CATEGORY}',
                     cookies=get_new_cookies)

    for item in r.json():
        if item['id'] != id_category and item['status'] == "1":
            id_category = item['id']
        else:
            continue

    assert r.status_code == 200


def test_create_record_success(get_new_cookies):
    global id_record
    global id_category_record

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}

    payload = {
        "name": str(''.join(random.choices(string.ascii_letters, k=8))),
        "url": 'http://localhost',
        "category_id": id_category
    }

    r = requests.post(f'{BASE_URL}{URL_RECORD}',
                      headers=headers,
                      json=payload,
                      cookies=get_new_cookies)

    id_record = r.json()['id']
    id_category_record = r.json()['category_id']

    assert r.status_code == 200


def test_get_new_category(get_new_cookies):
    global new_category_id

    r = requests.get(f'{BASE_URL}{URL_CATEGORY}',
                     cookies=get_new_cookies)

    for item in r.json():
        if item['id'] != id_category_record and item['status'] == "1":
            new_category_id = item['id']
        else:
            continue

    assert r.status_code == 200


def test_update_record_success(get_new_cookies):
    global new_name_record
    global new_url_record

    # id_category = get_random_category(id_category)
    new_name_record = ''.join(random.choices(string.ascii_letters, k=8))
    new_url_record = 'http://' + str(''.join(random.choices(string.ascii_letters, k=8)))

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}

    payload = {
        "name": new_name_record,
        "url": new_url_record,
        "category_id": new_category_id,
        "id": id_record
    }

    r = requests.patch(f'{BASE_URL}{URL_RECORD}',
                       headers=headers,
                       json=payload,
                       cookies=get_new_cookies)

    assert r.status_code == 200
    assert r.json()['name'] == new_name_record
    assert r.json()['url'] == new_url_record
    assert r.json()['category_id'] == new_category_id


def test_get_all_record_success(get_new_cookies):
    params = {
        "skip": 0,
        "limit": 100
    }

    r = requests.get(f'{BASE_URL}{URL_RECORD}',
                     params=params,
                     cookies=get_new_cookies)

    decision = False

    for item in r.json():
        if item['id'] == id_record:
            decision = True
            break
        else:
            continue

    assert r.status_code == 200
    assert decision is True


def test_get_one_record_success(get_new_cookies):
    r = requests.get(f'{BASE_URL}{URL_RECORD}/{id_record}',
                     cookies=get_new_cookies)

    assert r.status_code == 200
    assert r.json()['name'] == new_name_record
    assert r.json()['url'] == new_url_record
    assert r.json()['category_id'] == new_category_id


def test_delete_record_success(get_new_cookies):
    params = {
        'record_id': id_record
    }

    r = requests.delete(f'{BASE_URL}{URL_RECORD}',
                        params=params,
                        cookies=get_new_cookies)

    assert r.status_code == 204


def test_get_one_record_after_delete_success(get_new_cookies):
    r = requests.get(f'{BASE_URL}{URL_RECORD}/{id_record}',
                     cookies=get_new_cookies)

    assert r.status_code == 404

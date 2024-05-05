# imports pytest
# imports requests
#
# from tests.config imports URL_AUTH, BASE_URL, URL_CATEGORY
# from tests.test_back_list.conftest imports get_new_cookies
#
#
# @pytest.fixture()
# def get_random_category(get_new_cookies):
#     r = requests.get(f'{BASE_URL}{URL_CATEGORY}',
#                      cookies=get_new_cookies)
#
#     for item in r.json():
#         if item['id'] != id_category and item['status'] == "1":
#             print()
#             return item['id']
#         else:
#             continue
#
#     return None

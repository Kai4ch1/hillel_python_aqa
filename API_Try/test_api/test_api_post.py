import pytest

from hillel_python_aqa.API_Try.api_client.client_api import *

class TestApi:
    def test_request_get(self):
        api = RequestsClient()
        body = {
              "userId": 228,
              "title": "POST TRY",
              "body": "TEST BODY 228"
            }
        response = api.post_request(endpoint="/posts", payload=body)
        expected_result = {'body': 'TEST BODY 228',
                           'id': 101,
                           'title': 'POST TRY',
                           'userId': 228}
        actual_result = response.json()
        print(actual_result)
        assert response.status_code == 201
        assert expected_result == actual_result, f"the json isn`t as expected={actual_result}"

    @pytest.fixture
    def user_valid_body(self):
        return {'body': 'TEST BODY 228',
                           'id': 101,
                           'title': 'POST TRY',
                           'userId': 228}
    @pytest.mark.parametrize(
        "user_id, id_of_test, expected_status_code", [
                (13223232, "Valid", 201),
                ("32", "String Invalid", 400),
                (0, "Valid ID=0", 201),
                (0.1, "Invalid Decimal", 400),
                (-5, "Invalid Negative ID", 400),
                (True, "Bool Negative", 400),

        ])
    def test_user_id_field(self, user_id, id_of_test, user_valid_body, expected_status_code):
        api = RequestsClient()
        json_body = user_valid_body
        json_body["user_id"] = user_id
        response = api.post_request(endpoint="/posts", payload=json_body)
        actual_result = response.status_code
        assert actual_result == expected_status_code, (f"expected status code={expected_status_code}, but got status code={actual_result},\n "
                                                       f"and ID of test is{id_of_test}")




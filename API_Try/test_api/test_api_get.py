import pytest

from hillel_python_aqa.API_Try.api_client.client_api import *

class TestApi:
    def test_request_get(self):
        api = RequestsClient()
        response = api.get_request(endpoint="/posts/1")
        expected_result = {
              "userId": 1,
              "id": 1,
              "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
              "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            }
        actual_result = response.json()
        print(actual_result)
        assert response.status_code == 200
        assert expected_result == actual_result, f"the json isn`t as expected={actual_result}"

    @pytest.mark.smoke
    def test_status_code(self):
        api = RequestsClient()
        response = api.get_request(endpoint="/posts/1")
        assert response.status_code == 200, f"Expected status code 200, but got{response.status_code}"

    @pytest.mark.smoke()
    def test_fields_presence(self):
        api = RequestsClient()
        response = api.get_request(endpoint="/posts/1")
        payload: dict = response.json()
        assert "id" in payload, f"There`s no id in response`s json"
        assert "userId" in payload.keys(), f"There`s no userId in response`s json"
        assert "title" in payload.keys(), f"There`s no title in response`s json"
        assert "body" in payload.keys(), f"There`s no body in response`s json"



    @pytest.mark.smoke
    def test_consistency(self):
        api = RequestsClient()
        response = api.get_request(endpoint="/posts/1")
        payload: dict = response.json()
        assert len(payload["body"]) >= 100
        assert isinstance(payload["userId"], int)
        assert isinstance(payload["id"], int)

    @pytest.mark.skip(reason="unfinished tests")
    def test_unimplemented(self):
        pass
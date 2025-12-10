import pytest
import requests
import auth

from assertpy import soft_assertions, assert_that
from requests.auth import HTTPBasicAuth

from datetime import datetime

user_credentials = HTTPBasicAuth('test_user', 'test_pass')


class TestCars:

    @staticmethod
    def auth_token_controller():
        auth_token = auth.TestWrappedAuth(
            auth.HOST,
            "/auth",
            user_credentials
        )
        return auth_token.api_auth()['access_token']

    @pytest.fixture(scope="class")
    def get_auth_token(self):
        return self.auth_token_controller()

    def test_the_cars(self, get_auth_token):
        # initial smoke tests :3
        with soft_assertions():
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/cars")
            for key in response.json():
                assert_that(key).contains_key("brand").described_as(f"No 'Brand' key was found")
                assert_that(key).contains_key("engine_volume").described_as(f"No 'engine_volume' key was found")
                assert_that(key).contains_key("price").described_as(f"No 'price' key was found")
                assert_that(key).contains_key("year").described_as(f"No 'year' key was found")

    def test_sort_by_price(self, get_auth_token):
        with soft_assertions():
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/cars?sort_by=price")
            assert_that(response.status_code).is_equal_to(200).described_as(f"The status code should be 200, but got{response.status_code}")

            prices = [x["price"] for x in response.json()]
            for i in range(len(prices) - 1):
                next_element = i+1
                assert_that(prices[next_element]).is_greater_than_or_equal_to(prices[i]).described_as(f"The sorting working improperly, {prices[i]} could not be greater than {prices[next_element]}")

    def test_sort_by_brand(self, get_auth_token):
        with soft_assertions():
        # testing mandatory car brands
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/cars?sort_by=brand")
            assert_that(response.status_code).is_equal_to(200).described_as(f"The status code should be 200, but got{response.status_code}")
            brands = [x["brand"] for x in response.json()]
            assert_that(brands).contains("Nissan", "Audi", "Subaru", "Volvo", "Lexus", "Chevrolet", "Honda", "Hyundai", "Toyota").described_as("1 or more car brands missing")

    def test_sort_by_limit(self, get_auth_token):
        with soft_assertions():
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/cars?limit=10")
            assert_that(response.status_code).is_equal_to(200).described_as(f"The status code should be 200, but got{response.status_code}")
            car = [x for x in response.json()]
            assert_that(len(car)).is_less_than(11).described_as(f"Limit is broken, current pagination is set by current={len(car)}, "
                                                                f"expected to be lesser than 11")
    def test_sort_and_limit_by(self, get_auth_token):
        with soft_assertions():
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/cars?sort_by=year&limit=15")
            assert_that(response.status_code).is_equal_to(200).described_as(f"The status code should be 200, but got{response.status_code}")

            # Check that non-existent car year is not presented
            now = datetime.now().now().__str__()
            years = [x["year"] for x in response.json()]
            invalid_years = [2026, 2027, 2028]
            assert_that(years).does_not_contain(*invalid_years).described_as(f"Invalid car years {years} were found")
            # Check that amount of elements is equal to json length

            assert_that(len(years)).is_equal_to(len(response.json())).described_as("1 or more instances are out bounds of JSON length")
            engine_volume = [x["engine_volume"] for x in response.json()]

            # check the engine volume data type
            for engine in engine_volume:
                assert_that(engine).is_instance_of(float)

    def test_negative_endpoint(self, get_auth_token):
        with soft_assertions():
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/carss")
            assert_that(response.status_code).is_equal_to(404)

    def test_negative_sort_type(self, get_auth_token):
        # wrong sort type
        with soft_assertions():
            response = requests.get(headers={"Authorization": "Bearer " + get_auth_token}, url="http://127.0.0.1:8080/cars?sort_by=car")
            assert_that(response.status_code).is_equal_to(200)
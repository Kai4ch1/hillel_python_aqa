import requests

class RequestsClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.headers = {"Content-Type": "application/json"}

    def get_request(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params, headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            raise

    def post_request(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            raise

    def put_request(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(url, json=payload, headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            raise

    def delete_request(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, json=payload, headers=self.headers)
            return response
        except requests.exceptions.RequestException as e:
            raise





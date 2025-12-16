import requests

HOST = "http://127.0.0.1:8080"


class TestWrappedAuth:
    def __init__(self, url, auth_endpoint, auth_post_body):
        self.url = url
        self.auth_endpoint = auth_endpoint
        self.auth_post_body = auth_post_body


    def api_auth(self):
        with requests.Session() as s:
            response = s.post(self.url+self.auth_endpoint, auth=self.auth_post_body)
            data = response.json()

            return data
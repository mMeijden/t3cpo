import requests
import json
import hmac
import hashlib
from urllib.parse import urlencode


class Api(object):

    def __init__(self, key: str, secret: str, base_api_url: str = "https://api.3commas.io"):
        self.key = key
        self.secret = secret
        self.base_api_url = base_api_url

    def build_absolute_url(self, relative_path: str, query_params: str) -> str:
        return f'{self.base_api_url}{relative_path}{query_params}'

    def __sign_request(self, relative_path: str, params) -> str:
        encoded_secret = str.encode(self.secret)
        payload = str.encode(relative_path + params)
        return hmac.new(encoded_secret, payload, hashlib.sha256).hexdigest()

    def invoke(self, method, path, params=None):
        query_params = self.parse_query_params(params)
        absolute_url = self.build_absolute_url(path, query_params)
        sig = self.__sign_request(path, query_params)
        headers = {
            'APIKEY': self.key,
            'Signature': sig
        }
        response = requests.request(method=method,
                                    url=absolute_url,
                                    headers=headers)
        return response

    @staticmethod
    def parse_query_params(params: dict = None) -> str:
        if params:
            return f'?{urlencode(params)}'
        else:
            return ''

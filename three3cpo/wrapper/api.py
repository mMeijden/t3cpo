import requests
import json
import hmac
import hashlib


class Api(object):

    def __init__(self, key, secret):
        self.base_api_url = "https://api.3commas.io"
        self.key = key
        self.secret = secret

    def build_absolute_url(self, path: str) -> str:
        return f'{self.base_api_url}{path}'

    def sign_request(self, relative_path: str, params: None) -> str:
        params = '' if params is None else json.dumps(params)
        encoded_secret = str.encode(self.secret)
        payload = str.encode(relative_path + params)
        return hmac.new(encoded_secret, payload, hashlib.sha256).hexdigest()

    def invoke(self, method, path, params=None, **kwargs):
        sig = self.sign_request(path, params)
        absolute_url = self.build_absolute_url(path)
        headers = {
            'APIKEY': self.key,
            'Signature': sig
        }
        response = requests.request(method=method,
                                    url=absolute_url,
                                    headers=headers,
                                    **kwargs)
        return response


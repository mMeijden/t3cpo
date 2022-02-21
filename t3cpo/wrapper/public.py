import requests
from t3cpo.wrapper.api import Api


class PublicApi(Api):

    def __init__(self):
        super().__init__()
        self.relative_base = '/public/api/ver1'

    def invoke(self, method, path, params=None):
        query_params = self.parse_query_params(params)
        absolute_url = self.build_absolute_url(path, query_params)
        return requests.request(method=method, url=absolute_url)

    def ping(self) -> dict:
        return self.invoke('GET', f'{self.relative_base}/ping').json()

    def time(self) -> dict:
        return self.invoke('GET', f'{self.relative_base}/time').json()


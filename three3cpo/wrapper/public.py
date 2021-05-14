from wrapper.api import Api
import requests


class PublicApi(Api):

    def __init__(self):
        super().__init__()
        self.relative_base = '/public/api/ver1'

    def invoke(self, method, path, params=None):
        query_params = self.parse_query_params(params)
        absolute_url = self.build_absolute_url(path, query_params)
        response = requests.request(method=method,
                                    url=absolute_url)
        return response

    def ping(self):
        return self.invoke('GET', f'{self.relative_base}/ping').json()

    def time(self):
        return self.invoke('GET', f'{self.relative_base}/time').json()


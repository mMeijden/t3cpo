from wrapper.api import Api


class BotsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)

    def bots_pairs_blacklist(self):
        return super().invoke('GET', '/public/api/ver1/bots/pairs_black_list').json()

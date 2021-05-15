from t3cpo.wrapper.api import Api


class UsersApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/users'

    def change_mode(self, params):
        return self.invoke('POST', f'{self.relative_base}/change_mode', params=params).json()

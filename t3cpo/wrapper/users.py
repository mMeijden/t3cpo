from t3cpo.wrapper.api import Api


class UsersApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/users'

    def get_current_mode(self):
        return self.invoke('GET', f'{self.relative_base}/current_mode').json()

    def change_mode(self, params):
        return self.invoke('POST', f'{self.relative_base}/change_mode', params=params).json()

    def change_to_real_trading(self):
        return self.invoke('POST', f'{self.relative_base}/change_mode', params={'mode': 'real'}).json()

    def change_to_paper_trading(self):
        return self.invoke('POST', f'{self.relative_base}/change_mode', params={'mode': 'paper'}).json()

from t3cpo.wrapper.api import Api
from t3cpo.specs.user_api_spec import ChangeModeRequest


class UsersApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/users'

    def get_current_mode(self) -> dict:
        return self.invoke('GET', f'{self.relative_base}/current_mode').json()

    def change_mode(self, mode: str) -> bool:
        params = {
            'mode': mode
        }
        self._spec_fields(ChangeModeRequest, params)
        return self.invoke('POST', f'{self.relative_base}/change_mode', params=params).json()

    def change_to_real_trading(self) -> bool:
        return self.change_mode('real')

    def change_to_paper_trading(self) -> bool:
        return self.change_mode('paper')

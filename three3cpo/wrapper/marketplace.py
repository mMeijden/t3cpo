from three3cpo.wrapper.api import Api


class MarketPlaceApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/marketplace'

    def list_marketplace_items(self, params=None):
        return self.invoke('GET', f'{self.relative_base}/items', params=params).json()

    def get_item_signal(self, item_id: int, params=None):
        return self.invoke('GET', f'{self.relative_base}/{item_id}/signals', params=params).json()

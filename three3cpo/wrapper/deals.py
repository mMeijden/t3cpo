from three3cpo.wrapper.api import Api


class DealsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/deals'

    def deals(self, params=None):
        return self.invoke('GET', f'{self.relative_base}', params=params).json()

    def cancel_deal(self, deal_id: int):
        return self.invoke('POST', f'{self.relative_base}/{deal_id}/cancel').json()

    def update_deal(self, deal_id: int, params):
        return self.invoke('PATCH', f'{self.relative_base}/{deal_id}/update_deal', params=params).json()

    def panic_sell_deal(self, deal_id: int):
        return self.invoke('POST', f'{self.relative_base}/{deal_id}/panic_sell').json()

    def deal_info(self, deal_id: int):
        return self.invoke('GET', f'{self.relative_base}/{deal_id}/show').json()

    def cancel_manual_safety_order(self, deal_id: int, params):
        return self.invoke('POST', f'{self.relative_base}/{deal_id}/cancel_order', params=params).json()

    def deal_safety_orders(self, deal_id: int):
        return self.invoke('GET', f'{self.relative_base}/{deal_id}/market_orders').json()

    def add_manual_safety_order(self, deal_id: int, params):
        return self.invoke('POST', f'{self.relative_base}/{deal_id}/add_funds', params=params).json()

    def get_data_for_adding_funds(self, deal_id: int):
        return self.invoke('GET', f'{self.relative_base}/{deal_id}/data_for_adding_funds').json()

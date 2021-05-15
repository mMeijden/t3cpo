from t3cpo.wrapper.api import Api


class SmartTradesApiV2(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/v2/smart_trades'

    def get_smart_trade_history(self, params=None):
        return self.invoke('GET', f'{self.relative_base}', params=params).json()

    def create_smart_trade(self, params=None):
        return self.invoke('POST', f'{self.relative_base}', params=params).json()

    def get_smart_trade_by_id(self, smart_trade_id: int):
        return self.invoke('GET', f'{self.relative_base}/{smart_trade_id}').json()

    def cancel_smart_trade(self, smart_trade_id: int):
        return self.invoke('DELETE', f'{self.relative_base}/{smart_trade_id}').json()

    def update_smart_trade(self, smart_trade_id: int, params):
        return self.invoke('PATCH', f'{self.relative_base}/{smart_trade_id}', params=params).json()

    def add_funds(self, smart_trade_id: int, params):
        return self.invoke('POST', f'{self.relative_base}/{smart_trade_id}/add_funds', params=params).json()

    def close_smart_trade_market_price(self, smart_trade_id: int):
        return self.invoke('POST', f'{self.relative_base}/{smart_trade_id}/close_by_market').json()

    def force_start_smart_trade(self, smart_trade_id: int):
        return self.invoke('POST', f'{self.relative_base}/{smart_trade_id}/force_start').json()

    def force_process_smart_trade(self, smart_trade_id: int):
        return self.invoke('POST', f'{self.relative_base}/{smart_trade_id}/force_process').json()

    def set_note(self, smart_trade_id: int, params):
        return self.invoke('POST', f'{self.relative_base}/{smart_trade_id}/set_note', params=params).json()

    def get_smart_trade_trades(self, smart_trade_id: int):
        return self.invoke('GET', f'{self.relative_base}/{smart_trade_id}/trades').json()

    def panic_close_trade_market_price(self, smart_trade_id: int, trade_id: int):
        return self.invoke('POST', f'{self.relative_base}/{smart_trade_id}/trades/{trade_id}/close_by_market').json()

    def cancel_trade(self, smart_trade_id: int, trade_id: int):
        return self.invoke('DELETE', f'{self.relative_base}/{smart_trade_id}/trades/{trade_id}').json()

from wrapper.api import Api


class GridBotsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/grid_bots'

    def create_ai_grid_bot(self, params):
        return self.invoke('POST', f'{self.relative_base}/ai', params=params).json()

    def edit_ai_grid_bot(self, bot_id: int, params):
        return self.invoke('PATCH', f'{self.relative_base}/{bot_id}/ai', params=params).json()

    def create_manual_grid_bot(self, params):
        return self.invoke('POST', f'{self.relative_base}/manual', params=params).json()

    def edit_manual_grid_bot(self, bot_id: int, params):
        return self.invoke('PATCH', f'{self.relative_base}/{bot_id}/manual', params=params).json()

    def get_ai_settings(self, params):
        return self.invoke('POST', f'{self.relative_base}/manual', params=params).json()

    def list_grid_bots(self, params=None):
        return self.invoke('GET', f'{self.relative_base}', params=params).json()

    def get_grid_bot(self, bot_id: int):
        return self.invoke('GET', f'{self.relative_base}/{bot_id}').json()

    def delete_grid_bot(self, bot_id: int):
        return self.invoke('DELETE', f'{self.relative_base}/{bot_id}').json()

    def disable_grid_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/disable').json()

    def enable_grid_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/enable').json()

    def show_required_balance(self, bot_id:int):
        return self.invoke('GET', f'{self.relative_base}/{bot_id}/required_balances').json()

    def get_grid_bot_market_orders(self, bot_id: int):
        return self.invoke('GET', f'{self.relative_base}/{bot_id}/market_orders').json()

    def get_grid_bot_profits(self, bot_id: int):
        return self.invoke('GET', f'{self.relative_base}/{bot_id}/profits').json()

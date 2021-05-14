from wrapper.api import Api


class BotsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/bots'

    def bot_info(self, bot_id: int, params=None):
        return self.invoke('GET', f'{self.relative_base}/{bot_id}/show', params=params).json()

    def strategy_list(self, params=None):
        return self.invoke('GET', f'{self.relative_base}/strategy_list', params=params).json()

    def pairs_blacklist(self):
        return self.invoke('GET', f'{self.relative_base}/pairs_black_list').json()

    def update_pairs_blacklist(self, params):
        return self.invoke('POST', f'{self.relative_base}/update_pairs_black_list', params=params).json()

    def create_bot(self, params):
        return self.invoke('POST', f'{self.relative_base}/create_bot', params=params).json()

    def edit_bot(self, bot_id: int, params):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/update', params=params).json()

    def delete_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/delete').json()

    def disable_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/disable').json()

    def enable_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/enable').json()

    def list_bots(self, params=None):
        return self.invoke('GET', f'{self.relative_base}', params=params).json()

    def start_new_deal_asap(self, bot_id: int, params=None):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/start_new_deal', params=params).json()

    def list_bots_stats(self, params=None):
        return self.invoke('GET', f'{self.relative_base}/stats', params=params).json()

    def panic_sell_all_deals_for_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/panic_sell_all_deals').json()

    def cancel_all_deals_for_bot(self, bot_id: int):
        return self.invoke('POST', f'{self.relative_base}/{bot_id}/cancel_all_deals').json()

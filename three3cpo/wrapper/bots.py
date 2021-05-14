from wrapper.api import Api


class BotsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)

    def bot_info(self, bot_id: int, params=None):
        return self.invoke('GET', f'/public/api/ver1/bots/{bot_id}/show', params=params).json()

    def strategy_list(self, params=None):
        return self.invoke('GET', '/public/api/ver1/bots/strategy_list', params=params).json()

    def pairs_blacklist(self):
        return self.invoke('GET', '/public/api/ver1/bots/pairs_black_list').json()

    def update_pairs_blacklist(self, params):
        return self.invoke('POST', '/public/api/ver1/bots/update_pairs_black_list', params=params).json()

    def create_bot(self, params):
        return self.invoke('POST', '/public/api/ver1/bots/create_bot', params=params).json()

    def edit_bot(self, bot_id: int, params):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/update', params=params).json()

    def delete_bot(self, bot_id: int):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/delete').json()

    def disable_bot(self, bot_id: int):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/disable').json()

    def enable_bot(self, bot_id: int):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/enable').json()

    def list_bots(self, params=None):
        return self.invoke('GET', '/public/api/ver1/bots', params=params).json()

    def start_new_deal_asap(self, bot_id: int, params=None):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/start_new_deal', params=params).json()

    def list_bots_stats(self, params=None):
        return self.invoke('GET', '/public/api/ver1/bots/stats', params=params).json()

    def panic_sell_all_deals_for_bot(self, bot_id: int):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/panic_sell_all_deals').json()

    def cancel_all_deals_for_bot(self, bot_id: int):
        return self.invoke('POST', f'/public/api/ver1/bots/{bot_id}/cancel_all_deals').json()

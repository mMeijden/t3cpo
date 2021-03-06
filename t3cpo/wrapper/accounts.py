from t3cpo.wrapper.api import Api


class AccountsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)
        self.relative_base = '/public/api/ver1/accounts'

    def get_accounts(self):
        return self.invoke('GET', f'{self.relative_base}').json()

    def transfer(self, params: dict):
        return self.invoke('POST', f'{self.relative_base}/transfer', params=params).json()

    def transfer_history(self, params: dict):
        return self.invoke('GET', f'{self.relative_base}/transfer_history', params=params).json()

    def transfer_data(self):
        return self.invoke('GET', f'{self.relative_base}/transfer_data').json()

    def new_account(self, params: dict):
        return self.invoke('POST', f'{self.relative_base}/new', params=params).json()

    def edit_account(self, params: dict):
        return self.invoke('POST', f'{self.relative_base}/update', params=params).json()

    def market_list(self):
        return self.invoke('GET', f'{self.relative_base}/market_list').json()

    def market_pairs(self, params: dict):
        return self.invoke('GET', f'{self.relative_base}/market_pairs', params).json()

    def currency_rates(self, params: dict):
        return self.invoke('GET', f'{self.relative_base}/currency_rates', params).json()

    def deposit_data(self, account_id: int, params: dict):
        return self.invoke('GET', f'{self.relative_base}/{account_id}/deposit_data', params).json()

    def networks_info(self, account_id: int, params: dict = None):
        return self.invoke('GET', f'{self.relative_base}/{account_id}/networks_info', params).json()

    def convert_dust_to_bnb(self, account_id: int, params: dict = None):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/convert_dust_to_bnb', params).json()

    def active_trading_entities(self, account_id: int):
        return self.invoke('GET', f'{self.relative_base}/{account_id}/active_trading_entities').json()

    def sell_all_to_usd(self, account_id: int):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/sell_all_to_usd').json()

    def sell_all_to_btc(self, account_id: int):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/sell_all_to_btc').json()

    def balance_chart_data(self, account_id: int, params):
        return self.invoke('GET', f'{self.relative_base}/{account_id}/balance_chart_data', params).json()

    def load_balances(self, account_id: int):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/load_balances').json()

    def rename_exchange_connection(self, account_id: int, params):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/rename', params).json()

    def pie_chart_data(self, account_id: int):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/pie_chart_data').json()

    def account_table_data(self, account_id: int):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/account_table_data').json()

    def remove_exchange_connection(self, account_id: int):
        return self.invoke('POST', f'{self.relative_base}/{account_id}/remove').json()

    def account_leverage_data(self, account_id: int):
        return self.invoke('GET', f'{self.relative_base}/{account_id}/leverage_data').json()

    def account_info(self, account_id: int):
        return self.invoke('GET', f'{self.relative_base}/{account_id}').json()

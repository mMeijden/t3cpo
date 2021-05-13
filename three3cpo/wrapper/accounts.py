from wrapper.api import Api


class AccountsApi(Api):

    def __init__(self, key, secret):
        super().__init__(key, secret)

    def list(self):
        return self.invoke('GET', '/public/api/ver1/accounts').json()

    # POST /ver1/accounts/transfer
    def transfer(self, currency: str, amount: float, to_account_id: int, from_account_id: int):
        payload = {
            'currency': currency,
            'amount': amount,
            'to_account_id': to_account_id,
            'from_account_id': from_account_id
        }
        return self.invoke('POST', '/public/api/ver1/accounts/transfer', params=payload).json()

    # GET /ver1/accounts/transfer_history
    def transfer_history(self, account_id: int, currency: str, page: int = 1, per_page: int = 10):
        payload = {
            'account_id': account_id,
            'currency': currency,
            'page': page,
            'per_page': per_page
        }
        return self.invoke('GET', '/public/api/ver1/accounts/transfer_history', params=payload).json()

    # GET /ver1/accounts/transfer_data
    def transfer_data(self):
        return self.invoke('GET', '/public/api/ver1/accounts/transfer_data').json()

    # POST /ver1/accounts/new
    def new_account(self, account_type: str, name: str, **kwargs):
        payload = {
            'type': account_type,
            'name': name,
            **kwargs
        }
        return self.invoke('POST', '/public/api/ver1/accounts/new', params=payload).json()

    # POST /ver1/accounts/update
    def edit_account(self, account_id: int, **kwargs):
        payload = {
            'account_id': account_id,
            **kwargs
        }
        return self.invoke('POST', '/public/api/ver1/accounts/new', params=payload).json()

    # GET /ver1/accounts/market_pairs
    def market_pairs(self):
        pass

    # GET /ver1/accounts/currency_rates
    # GET /ver1/accounts/{account_id}/deposit_data
    # GET /ver1/accounts/{account_id}/networks_info
    # POST /ver1/accounts/{account_id}/convert_dust_to_bnb
    # GET /ver1/accounts/{account_id}/active_trading_entities
    # POST /ver1/accounts/{account_id}/sell_all_to_usd
    # POST /ver1/accounts/{account_id}/sell_all_to_btc
    # GET /ver1/accounts/{account_id}/balance_chart_data
    # POST /ver1/accounts/{account_id}/load_balances
    # POST /ver1/accounts/{account_id}/rename
    # POST /ver1/accounts/{account_id}/pie_chart_data
    # POST /ver1/accounts/{account_id}/account_table_data
    # POST /ver1/accounts/{account_id}/remove
    # GET /ver1/accounts/{account_id}/leverage_data
    # GET /ver1/accounts/{account_id}

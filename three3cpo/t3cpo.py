from wrapper.bots import BotsApi
from wrapper.accounts import AccountsApi
from wrapper.deals import DealsApi
from wrapper.grid_bots import GridBotsApi
from wrapper.marketplace import MarketPlaceApi


class Three3Cpo(object):

    def __init__(self, key, secret):
        self.Bots = BotsApi(key=key, secret=secret)
        self.Accounts = AccountsApi(key=key, secret=secret)
        self.Deals = DealsApi(key=key, secret=secret)
        self.GridBots = GridBotsApi(key=key, secret=secret)
        self.MarketPlace = MarketPlaceApi(key=key, secret=secret)

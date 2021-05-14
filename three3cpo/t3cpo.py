from wrapper.bots import BotsApi
from wrapper.accounts import AccountsApi
from wrapper.deals import DealsApi
from wrapper.grid_bots import GridBotsApi
from wrapper.marketplace import MarketPlaceApi
from wrapper.smarttrades import SmartTradesApiV2
from wrapper.users import UsersApi
from wrapper.public import PublicApi


class Three3Cpo(object):

    def __init__(self, key, secret):
        self.Public = PublicApi()
        self.Bots = BotsApi(key=key, secret=secret)
        self.Accounts = AccountsApi(key=key, secret=secret)
        self.Deals = DealsApi(key=key, secret=secret)
        self.GridBots = GridBotsApi(key=key, secret=secret)
        self.MarketPlace = MarketPlaceApi(key=key, secret=secret)
        self.SmartTradesV2 = SmartTradesApiV2(key=key, secret=secret)
        self.Users = UsersApi(key=key, secret=secret)

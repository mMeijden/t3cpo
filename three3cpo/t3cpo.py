from three3cpo.wrapper import PublicApi, BotsApi, AccountsApi, DealsApi, GridBotsApi, MarketPlaceApi, SmartTradesApiV2, UsersApi


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

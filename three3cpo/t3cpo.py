from wrapper.bots import BotsApi
from wrapper.accounts import AccountsApi
from wrapper.deals import DealsApi


class Three3Cpo(object):

    def __init__(self, key, secret):
        self.bots = BotsApi(key=key, secret=secret)
        self.accounts = AccountsApi(key=key, secret=secret)
        self.deals = DealsApi(key=key, secret=secret)

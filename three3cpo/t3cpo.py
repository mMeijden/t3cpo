from wrapper import bots
from wrapper import accounts


class Three3Cpo(object):

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.bots = bots.BotsApi(key=self.key, secret=self.secret)
        self.accounts = accounts.AccountsApi(key=self.key, secret=self.secret)
# T3CPO
T3CPO is an unofficial python wrapper of the 3Commas API. \
For more information about the original API please visit the [official API docs](https://github.com/3commas-io/3commas-official-api-docs/) or [3Commas support](https://support.3commas.io/hc/en-us) for further reference.

```bash
pip install t3cpo
```

##Basic Usage
Using T3CPO is simple.
```python
from t3cpo import T3CPO

# provide T3CPO the key and the secret from 3Commas.
t3c = T3CPO(key='', secret='')

# T3CPO consists out of multiple API Wrappers which can be called individually. For example:
bots_blacklist = t3c.Bots.pairs_blacklist()

# Basic endpoints with only optional parameters can be invoked:
bots_info = t3c.Bots.list_bots()

# Optional parameters can be provided as a dict
single_bots_info = t3c.Bots.list_bots({'limit': 1})
t3c.Users.change_mode({'mode': 'paper'})

# Some endpoints require alternative information such as a trade_id or an account_id
specific_info = t3c.Bots.bot_info(123456)
account_info = t3c.Accounts.account_info(123)

# Besides a required id, optional parameters can be provided as a dict. The optional dict is always the last argument.
deposit_info = t3c.Accounts.networks_info(987654, {'purpose': 'deposit'})
```

##Advanced usage
It's also possible to only use a single API wrapper for any particular reason.
E.g. if you would like to combine multiple API credentials from 3Commas that have a different read/write model.

Example using only the BotsApi
```python
from t3cpo.wrapper import BotsApi

t3c = BotsApi(key='', secret='')
blacklist = t3c.pairs_blacklist()
```

Example using only the AccountsApi
```python
from t3cpo.wrapper import AccountsApi
t3c = AccountsApi(key='', secret='')
account_info = t3c.account_info(123456)
```
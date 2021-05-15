import unittest
from unittest import mock
from t3cpo.wrapper import UsersApi


class TestUsersApi(unittest.TestCase):

    @mock.patch('requests.request')
    def test_user_mode(self, mock_request: mock.MagicMock):
        bot = UsersApi('testKey', 'youshallnotpass')
        bot.change_mode({'mode': 'paper'})
        mock_request.assert_called_with(
            method='POST',
            url="https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper",
            headers={
                'APIKEY': 'testKey',
                'Signature': '7752c2b45165eaaf2846f53f626feae1da758883f621677ba1c57444a4085505'
            })

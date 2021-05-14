import unittest
from unittest import mock

from three3cpo.wrapper import PublicApi


class TestPublicApi(unittest.TestCase):

    @mock.patch('requests.request')
    def test_public_ping(self, mock_request: mock.MagicMock):
        bot = PublicApi()
        bot.ping()
        mock_request.assert_called_with(method='GET', url='https://api.3commas.io/public/api/ver1/ping')

    @mock.patch('requests.request')
    def test_public_time(self, mock_request: mock.MagicMock):
        bot = PublicApi()
        bot.time()
        mock_request.assert_called_with(method='GET', url='https://api.3commas.io/public/api/ver1/time')

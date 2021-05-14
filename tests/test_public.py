import unittest
from three3cpo import wrapper
from unittest import mock


class TestPublicApi(unittest.TestCase):

    @mock.patch('requests.request')
    def test_public_ping(self, mock_request: mock.MagicMock):
        bot = wrapper.public.PublicApi()
        bot.ping()
        mock_request.assert_called_with(method='GET', url='https://api.3commas.io/public/api/ver1/ping')

    @mock.patch('requests.request')
    def test_public_time(self, mock_request: mock.MagicMock):
        bot = wrapper.public.PublicApi()
        bot.time()
        mock_request.assert_called_with(method='GET', url='https://api.3commas.io/public/api/ver1/time')


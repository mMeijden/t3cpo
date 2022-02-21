import unittest
from t3cpo.wrapper import UsersApi
import responses


class TestUsersApi(unittest.TestCase):

    def setUp(self):
        self.t3c = UsersApi('testKey', 'youshallnotpass')

    @responses.activate
    def test_change_mode_paper(self):
        responses.add(method=responses.POST,
                      url='https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper',
                      json={'error': 'not found'},
                      status=200)

        self.t3c.change_mode(mode='paper')
        expected_url = 'https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url

    @responses.activate
    def test_change_mode_real(self):
        responses.add(method=responses.POST,
                      url='https://api.3commas.io/public/api/ver1/users/change_mode?mode=real',
                      json={'error': 'not found'},
                      status=200)

        self.t3c.change_mode(mode='real')

        expected_url = 'https://api.3commas.io/public/api/ver1/users/change_mode?mode=real'
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url

    @responses.activate
    def test_change_to_real_trading_mode(self):
        responses.add(method=responses.POST,
                      url='https://api.3commas.io/public/api/ver1/users/change_mode?mode=real',
                      json={'error': 'not found'},
                      status=200)

        self.t3c.change_to_real_trading()

        expected_url = 'https://api.3commas.io/public/api/ver1/users/change_mode?mode=real'
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url

    @responses.activate
    def test_change_to_paper_trading_mode(self):
        responses.add(method=responses.POST,
                      url='https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper',
                      json={'error': 'not found'},
                      status=200)

        self.t3c.change_to_paper_trading()
        expected_url = 'https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper'
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url

import unittest
from unittest import mock
from t3cpo.wrapper import UsersApi
import responses


class TestUsersApi(unittest.TestCase):

    @responses.activate
    def test_user_mode(self):
        responses.add(method=responses.POST,
                      url='https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper',
                      json={'error': 'not found'},
                      status=200)
        t3c = UsersApi('testKey', 'youshallnotpass')
        t3c.change_mode({'mode': 'paper'})

        expected_url = 'https://api.3commas.io/public/api/ver1/users/change_mode?mode=paper'
        expected_key = 'testKey'
        expected_sig = '7752c2b45165eaaf2846f53f626feae1da758883f621677ba1c57444a4085505'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url
        assert responses.calls[0].request.method == 'POST'
        assert responses.calls[0].request.headers['APIKEY'] == expected_key
        assert responses.calls[0].request.headers['Signature'] == expected_sig

import unittest
from t3cpo import T3CPO
import responses


class TestT3Cpo(unittest.TestCase):

    @responses.activate
    def test_T3cpo_UsersApi(self):
        responses.add(method=responses.POST,
                      url='https://api.3commas.io/public/api/ver1/users/change_mode?mode=real',
                      json={'error': 'not found'},
                      status=200)
        t3c = T3CPO('testKey', 'youshallnotpass')
        t3c.Users.change_mode({'mode': 'real'})

        expected_url = 'https://api.3commas.io/public/api/ver1/users/change_mode?mode=real'
        expected_key = 'testKey'
        expected_sig = 'e7db6bae980f81e1a05cc4b4f8849e92b5c189134c45f2274f1df915e35297fa'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url
        assert responses.calls[0].request.method == 'POST'
        assert responses.calls[0].request.headers['APIKEY'] == expected_key
        assert responses.calls[0].request.headers['Signature'] == expected_sig

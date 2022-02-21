import unittest
from unittest import mock
from dataspec import s
from spec_helper import parse_spec_to_readable_message
from t3cpo.wrapper import PublicApi


class TestSpecHelper(unittest.TestCase):


    def test_nested(self):
        mode = s("mode", {'real', 'paper'})
        ChangeModeRequest = s('change_mode_request', {'mode': mode})
        params = {
            'mode': {
                'mode': 'paper'
            }
        }
        validation = s.explain(ChangeModeRequest,params)
        explanation = parse_spec_to_readable_message(validation)
        print(explanation)

    # @mock.patch('requests.request')
    # def test_public_time(self, mock_request: mock.MagicMock):
    #     bot = PublicApi()
    #     bot.time()
    #     mock_request.assert_called_with(method='GET', url='https://api.3commas.io/public/api/ver1/time')

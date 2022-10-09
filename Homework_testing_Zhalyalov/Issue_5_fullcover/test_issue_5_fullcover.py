from Issue_5_fullcover import what_is_year_now
from unittest.mock import patch, Mock
import pytest


def test_what_is_year_now():
    with patch("Issue_5_fullcover.urllib.request.urlopen") as mocked_url_request:
        http_response_mock = Mock()
        http_response_mock.read = lambda: '{"currentDateTime": "2022-10-05T20:55Z"}'
        mocked_url_request.return_value.__enter__ = lambda _: http_response_mock

        assert what_is_year_now() == 2022
        mocked_url_request.assert_called_once()


def test_what_is_year_now2():
    with patch("Issue_5_fullcover.urllib.request.urlopen") as mocked_url_request:
        http_response_mock = Mock()
        http_response_mock.read = lambda: '{"currentDateTime": "2022/10/05T20:55Z"}'
        mocked_url_request.return_value.__enter__ = lambda _: http_response_mock

        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_url_request.assert_called_once()


def test_what_is_year_now3():
    with patch("Issue_5_fullcover.urllib.request.urlopen") as mocked_url_request:
        http_response_mock = Mock()
        http_response_mock.read = lambda: '{"currentDateTime": "01.03.2022T20:55Z"}'
        mocked_url_request.return_value.__enter__ = lambda _: http_response_mock

        assert what_is_year_now() == 2022
        mocked_url_request.assert_called_once()

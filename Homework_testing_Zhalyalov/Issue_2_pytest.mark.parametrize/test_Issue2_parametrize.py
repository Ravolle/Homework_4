from Issue_2_parametrize import decode
import pytest


@pytest.mark.parametrize(
    "source_string,result",
    [
        ('-.-. .-. .. -. --. .', 'CRINGE'),
        ('.- .-. - ..- .-. .---- ..--- ----- ---..', 'ARTUR1208'),
        (' ', ''),
        ('-.--. -.--.-', '()'),
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result

from Issue_4_pytest import fit_transform
import pytest


def test_len_raises_type_error():
    with pytest.raises(TypeError):
        fit_transform()


def test_fit_numbers():
    expected = [
        ('123', [0, 0, 0, 1]),
        ('321', [0, 0, 1, 0]),
        ('123', [0, 0, 0, 1]),
        ('546', [0, 1, 0, 0]),
        ('555', [1, 0, 0, 0]),
        ('123', [0, 0, 0, 1])
    ]
    assert fit_transform(['123', '321', '123', '546', '555', '123']) == expected


def test_fit_cities():
    expected1 = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(['Moscow', 'New York', 'Moscow', 'London']) == expected1


def test_fit_mixed():
    expected2 = [
        ('Mo2sco3w', [0, 0, 1]),
        ('New1_York4', [0, 1, 0]),
        ('Mo2sco3w', [0, 0, 1]),
        ('Lond_on', [1, 0, 0]),
    ]
    assert fit_transform(['Mo2sco3w', 'New1_York4', 'Mo2sco3w', 'Lond_on']) == expected2

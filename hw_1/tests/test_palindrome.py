import pytest
from hw_1.src.palindrome import defines_palindrome

data_test_positive = [(121, True),
                      (100, False),
                      (1234567654321, True),
                      (2137, False)]

@pytest.mark.parametrize('val, result', data_test_positive)
def test_palindrome_positive(val, result):
    assert defines_palindrome(val) == result

data_test_negative = [('', pytest.raises(TypeError)),
                      ('qwer', pytest.raises(TypeError)),
                      (bool, pytest.raises(TypeError)),
                      (45.7, pytest.raises(TypeError)),
                      ([''], pytest.raises(TypeError)),
                      (0, pytest.raises(ValueError)),
                      (78, pytest.raises(ValueError)),]

@pytest.mark.parametrize('val, result', data_test_negative)
def test_palindrome_negative(val, result):
    with result:
        assert defines_palindrome(val) == result

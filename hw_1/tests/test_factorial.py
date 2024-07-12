import pytest
from hw_1.src.factorial import calculation_factorial_number

data_test_positive = [(5, 120),
                      (7, 5040),
                      (1, 1),
                      (0, 1)]

@pytest.mark.parametrize('val, result', data_test_positive)
def test_factorial_positive(val, result):
    assert calculation_factorial_number(val) == result

data_test_negative = [('qwer', pytest.raises(TypeError)),
                      ('', pytest.raises(TypeError)),
                      (bool, pytest.raises(TypeError)),
                      (4.5, pytest.raises(TypeError)),
                      (None, pytest.raises(TypeError)),
                      ([], pytest.raises(TypeError)),
                      (-7, pytest.raises(ValueError)),
                      (21, pytest.raises(ValueError))]

@pytest.mark.parametrize('val, result', data_test_negative)
def test_factorial_negative(val, result):
    with result:
        assert calculation_factorial_number(val) == result

import pytest
from hw_1.src.fibonacci import calculation_fibonacci_numbers

data_test_positive = [(10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
                      (5, [1, 1, 2, 3, 5, 8]),
                      (0, [1]),
                      (17, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584])]

@pytest.mark.parametrize('val, result', data_test_positive)
def test_fibonacci_positive(val, result):
    assert calculation_fibonacci_numbers(val) == result

data_test_negative = [('qwer', pytest.raises(TypeError)),
                      ('', pytest.raises(TypeError)),
                      (bool, pytest.raises(TypeError)),
                      (4.5, pytest.raises(TypeError)),
                      (None, pytest.raises(TypeError)),
                      ([], pytest.raises(TypeError)),
                      (-7, pytest.raises(ValueError))]

@pytest.mark.parametrize('val, result', data_test_negative)
def test_fibonacci_negative(val, result):
    with result:
        assert calculation_fibonacci_numbers(val) == result
import pytest
from hw_1.src.count_ones import count_ones
data_test_positive = [(156, 4),
                      (17, 2),
                      (240, 4),
                      (2478, 7)]
@pytest.mark.parametrize('val, result', data_test_positive)
def test_count_ones_positive(val, result):
    assert count_ones(val) == result

data_test_negative = [(None, pytest.raises(TypeError)),
                      (bool, pytest.raises(TypeError)),
                      ('', pytest.raises(TypeError)),
                      ('qwer', pytest.raises(TypeError)),
                      (-7, pytest.raises(ValueError))]

@pytest.mark.parametrize('val, result', data_test_negative)
def test_count_ones_negative(val, result):
    with result:
        assert count_ones(val) == result


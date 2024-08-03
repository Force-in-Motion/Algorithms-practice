import pytest
from buble_sort.main import create_arr_numbers

data_test_positive = [('1 2 4 7 9', ['1', '2', '4', '7', '9']),
                      ('9 1 5 8 5', ['9', '1', '5', '8', '5'])]

@pytest.mark.cr_arr_nums_pos
@pytest.mark.parametrize('data, result', data_test_positive)
def test_create_arr_numbers_positive(data, result):

    assert create_arr_numbers(data) == result


data_test_negative = [(bool, pytest.raises(TypeError)),
                                         (int, pytest.raises(TypeError)),
                                         (float, pytest.raises(TypeError)),
                                         (dict, pytest.raises(TypeError)),
                                         ('', pytest.raises(ValueError))]

@pytest.mark.cr_arr_nums_neg
@pytest.mark.parametrize('data, result', data_test_negative)
def test_create_arr_numbers_negative(data, result):
    with result:
        assert create_arr_numbers(data) == result

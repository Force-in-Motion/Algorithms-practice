
def calculation_fibonacci_numbers(n) -> list:
    """
    Создает список чисел финабучи, если проверки пройдены
    :param n: Пренимает целое число
    :return: Возвращает список чисел финабучи
    """
    if not isinstance(n, int):
        raise TypeError('Получен не верный тип данных, ожидалось целое число')

    if n < 0:
        raise ValueError('Передаваемое значение не может быть отрицательным')

    lst_fibonacci_nums = []
    fib_num_a = 0
    fib_num_b = 1

    for i in range(0, n+1, 1):
        fib_num_a, fib_num_b = fib_num_b, fib_num_a + fib_num_b
        lst_fibonacci_nums.append(fib_num_a)
    return lst_fibonacci_nums





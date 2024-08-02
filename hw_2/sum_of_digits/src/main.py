

def create_number(data: str) -> int or bool:
    """
    Из полученной строки формирует список элементов, выполняет проверку, что все элементы являются целыми числами,
    затем список чисел преобразует в единое целое число и увеличивает его на 1
    :param data: Пренимает строку целых чисел
    :return: Возвращает целое единое число
    """
    lst_str = data.split()

    for i in lst_str:
        if not i.isdigit():
            return False

    number = int(''.join(lst_str))

    number += 1

    return number


def reversed_elems_arr(lst: list) -> list[int]:
    """
    Выполняет реверс полученного списка
    :param lst: Пренимает список целых чисел
    :return: Возвращает перевернутый список
    """

    assert isinstance(lst, list), TypeError('Получен не верный тип данных, ожидал список')

    for i in range(0, len(lst) // 2, 1):

        lst[i], lst[-1 - i] = lst[-1 - i], lst[i]

    return lst


def create_arr_nums(data: int) -> list[int]:
    """
    Преобразует целое число в список целых чисел, разбивая число на цифры, в своем теле вызывает 2 другие функции
    :param data: Пренимает строку целых чисел
    :return: Возвращает список целых чисел, готовый для вывода пользователю
    """

    assert isinstance(data, int), TypeError('Получен не верный тип данных, ожидалось целое число')

    lst = []

    while data != 0:
        lst.append(data % 10)

        data //= 10


    return lst

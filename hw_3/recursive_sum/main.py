
def create_arr_numbers(data: str) -> list[float or int] or bool:
    """
    Пренимает данные и при соблюдении условия создает список, затем преобразует каждый элемент в целое число и добавлляет в новый список
    :param data: Пренимает строку
    :return: Возвращает список целых чисел
    """
    lst_int = []

    if not isinstance(data, str): raise TypeError()

    if data == '': raise ValueError()

    lst = data.split()

    for i in lst:
        if not i.isdigit():
            return False
        lst_int.append(int(i))

    return lst_int


def recursive_sum(arr: list, ) -> int or list:
    """
    Вычисляет сумму элементов полученного массива
    :param arr: Пренимает массив целых чисел
    :return: Возвращает сумму элементов массива
    """

    if not isinstance(arr, list): raise TypeError()

    if len(arr) == 0: return arr

    if len(arr) == 1:
        return arr[0]

    return arr[0] + recursive_sum(arr[1:])






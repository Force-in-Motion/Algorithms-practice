
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


def recursive_max(arr: list, ) -> int or list:
    """
    Вычисляет максимальный элемент массива
    :param arr: Пренимает массив целых чисел
    :return: Возвращает сумму элементов массива
    """

    if not isinstance(arr, list): raise TypeError()

    if len(arr) == 0: return 0

    if len(arr) == 1:
        return arr[0]

    max_num = recursive_max(arr[1:])

    return arr[0] if arr[0] > max_num else max_num






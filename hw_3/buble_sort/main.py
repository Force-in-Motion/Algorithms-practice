
def create_arr_numbers(data: str) -> list[float] or bool:
    """
    Пренимает данные и при соблюдении условия создает список
    :param data: Пренимает строку
    :return: Возвращает список строк
    """
    if not isinstance(data, str): raise TypeError()

    if data == '': raise ValueError()

    lst = data.split()

    for i in lst:
        if not i.isdigit():
            return False

    return lst


def bubble_sort(arr: list, key=lambda x: float(x), order_by=lambda x, y: x < y) -> list:
    """
    Пренимает массив строк, сортирует согласно заданному признаку сортировки
    :param arr: Пренимает массив строк
    :param key: Пренимает функцию - ключ
    :param order_by: Пренимает функцию, задающую признак сортировки
    :return: Возвращает сортированный массив
    """

    if not isinstance(arr, list): raise TypeError()

    if len(arr) == 0 or len(arr) == 1: return arr

    for i in range(0, len(arr)-1, 1):

        for j in range(0, len(arr)-i-1, 1):

            if order_by(key(arr[j]), key(arr[j+1])):

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


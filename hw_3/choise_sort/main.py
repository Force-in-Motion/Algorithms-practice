
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


def choise_sort(arr: list, condition=lambda x, y: x < y, key=lambda x: int(x)) -> type(any):
    """
    Пренимает массив строк, сортирует согласно заданному признаку сортировки
    :param arr: Пренимает массив строк
    :return: Возвращает сортированный массив
    """
    count_comparisons = 0
    count_exchange = 0

    if not isinstance(arr, list): raise TypeError()

    if len(arr) == 0 or len(arr) == 1: return arr

    for i in range(0, len(arr)-1, 1):
        index_min = i

        for j in range(i, len(arr), 1):
            if condition(key(arr[index_min]), key(arr[j])):
                index_min = j
                count_comparisons += 1

        arr[i], arr[index_min] = arr[index_min], arr[i]
        count_exchange += 1

    return arr, count_comparisons, count_exchange


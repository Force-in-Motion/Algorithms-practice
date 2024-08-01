
def create_lst_int_from_input_data(data: str) -> list[int]:
    """
    Проверяет полученную строку на возможность концертации элементов в целые числа, если данные соответствуют то конвертирует их в целые числа и создает из них список
    :param data: Пренимает строку
    :return: Вохвращает список чисел, или False
    """
    lst_nums = data.split()

    lst = []

    for i in lst_nums:
        if not i.isdigit():
            return False
        lst.append(int(i))

    return lst


def convert_data(data: str) -> int:
    """
    Конвертирует Полученные данные в целые числа
    :return: Возвращает целые числа
    """
    data = int(data)
    return data


def revert_array(lst: list, k: int) -> list[int]:
    """
    Сначала выполняет сдвиг эдементов массива на k значение, затем выполняет реыерс элементов массива
    :param arr: Пренимает массив целых чисел
    :param k: Пренимает значение, на которое нужно выполнить сдвиг
    :return: Возвращает новый массив
    """
    length = len(lst)

    arr = lst[-k:] + lst[:-k]

    for i in range(0, length // 2, 1):
        arr[i], arr[length-1-i] = arr[length-1-i], arr[i]

    return arr


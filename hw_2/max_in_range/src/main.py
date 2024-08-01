
def create_lst_int_from_input_data(data):
    """
    Преобразует полученную строку в список целых чисел
    :param data: Пренимает строку
    :return: Возвращает список целых чисел
    """
    arr = [int(i) for i in data if i.isdigit()]
    return arr

def convert_data(start, end):
    """
    Конвертирует Полученные данные в целые числа
    :return: Возвращает целые числа
    """
    start = int(start)
    end = int(end)
    return start, end

def max_in_range(arr: list, start, end) -> (int or float, int):
    """
    Вычисляет максимальный элемент в списке целых чисел и находит относительную и абсолютную координату этого элемента
    :param arr: Пренимает список целых чисел
    :param start: Пренимает начальное значаение интервала поиска
    :param end: Пренимает конечное значаение интервала поиска
    :return: Возвращает  максимальный элемент и 2 его координаты
    """
    absolute_index = 0
    relative_index = 0
    max_num = 0

    for i in range(0, end+1, 1):
        if start <= i and i <= end:

            if max_num < arr[i]:
                max_num = arr[i]
                absolute_index = i

                if i == start:
                    relative_index = 0
                else:
                    relative_index += 1

    return (max_num, relative_index, absolute_index)




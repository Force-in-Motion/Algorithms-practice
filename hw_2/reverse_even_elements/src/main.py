
def create_lst_numbers(data: str) -> list[int] or bool:
    """
    Формирует шз полученных данных список целых чисел
    :param data: Пренимает строку данных
    :return: Список целых чисел
    """
    lst = []
    new_data = data.split()

    for i in new_data:
        if not i.isdigit():
            return False
        lst.append(int(i))

    return lst


def reverse_even_elements(lst: list[int]) -> list[int]:
    """
    Обходит полученный список и делает реверс четных чисел в порядке убывания,
    нечетные остаются на своих местах
    :param lst: Пренимает список целых чисел
    :return: Возвращает список с отсортированными четными числами в порядке убывания
    """
    for i in range(0, len(lst), 1):
        if lst[i] % 2 == 0:
            max_even = i

            for j in range(i, len(lst), 1):
                if lst[j] % 2 == 0 and lst[j] > lst[max_even]:
                    lst[max_even], lst[j] = lst[j], lst[max_even]

    return lst


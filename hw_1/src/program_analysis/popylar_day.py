

path = r'/hw_1/src/program_analysis/data_sql'


def read_data_file(path: str) -> list:
    """
    Считывает данные из файла и формирует из них список строк
    :param path: Пренимает путь к файлу
    :return: Возвращает список строк
    """
    with open(path, 'r') as f:
        data_file = f.read().split()
    return data_file


def build_matrix_data(data_file: list) -> list[list: str]:
    """
    Формирует матрицу строк из полученного списка строк
    :param data_file: Пренимает список строк
    :return: Возвращает матрицу строк
    """
    matrix_data = []

    for i in data_file:
        matrix_data.append(i.split(','))

    return matrix_data


def requests_count_visitors(min_value: str, max_value: str):
    """
    Запрашивает у пользователя значения, исходя из которых нужно отфильтровать данные
    :param min_value: Пренимает минимально возможное значение
    :param max_value: Пренимает максимально возможное значение
    :return: Возвращает значение, введенное пользователем, если оно прошло все проверки
    """
    count_visitors = input('Введите количество посетителей >> ')

    if count_visitors == '' or not count_visitors.isdigit():
        raise TypeError('Получен не верный тип данных, ожидалось целое число')

    if count_visitors < min_value or count_visitors > max_value:
        raise ValueError(f'Переданные значения не могут быть меньше {min_value} и больше {max_value}')

    return count_visitors


def check_min_values(matrix_data: list[list]) -> str:
    """
    Определяет минимально возможное значение из всей матрицы
    :param matrix_data: Пренимает матрицу строк
    :return: Возвращает минимально возможное значение
    """
    min_value = '9999999999999'

    for i in range(0, len(matrix_data), 1):
        if matrix_data[i][1] < min_value:
            min_value = matrix_data[i][1]

    return min_value

def check_max_value(matrix_data: list[list]) -> str:
    """
    Определяет максимально возможное значение из всей матрицы
    :param matrix_data: Пренимает матрицу строк
    :return: Возвращает максимально возможное значение
    """
    max_value = '0'

    for i in range(0, len(matrix_data), 1):
        if matrix_data[i][1] > max_value:
            max_value = matrix_data[i][1]

    return max_value

def determines_popular_days(matrix_data: list[list], count_visitors: str) -> list:
    """
    Создает список данных, определенных по запросу пользователя
    :param matrix_data: Пренимает матрицу строк
    :param count_visitors: Результат запроса пользователя
    :return: Возвращает список значений
    """
    lst_popular_days = []

    for i in range(0, len(matrix_data), 1):
        for j in range(0, len(matrix_data[i]), 1):
            if matrix_data[i][j] >= count_visitors:
                lst_popular_days.append(matrix_data[i])

    return lst_popular_days


def print_popular_days(popular_days: list) -> None:
    """
    Выводит на консоль список данных пользователя с пояснениями
    :param popular_days: Пренимает список данных пользователя
    :return: None
    """
    print('Популярные дни указанного диапазона:', end='\n')
    for i in range(0, len(popular_days), 1):
        print(f'{popular_days[i][0]}, количество посетителей: {popular_days[i][1]} ')


data_file = read_data_file(path)
matrix_data = build_matrix_data(data_file)
min_value = check_min_values(matrix_data)
max_value = check_max_value(matrix_data)
count_visitors = requests_count_visitors(min_value, max_value)
popular_days = determines_popular_days(matrix_data, count_visitors)
print_popular_days = print_popular_days(popular_days)

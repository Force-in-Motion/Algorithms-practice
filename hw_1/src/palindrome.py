

def defines_palindrome(x):
    lst = []

    if not isinstance(x, int):
        raise TypeError('Получен не верный тип данных, ожидалось целое число')

    if not len(str(x)) > 2:
        raise ValueError('Для проверки на полиндром число не может иметь меньше 3 цифр')

    if x < 0:
        raise ValueError('Отрицательное число не может быть палиндромом')

    while x != 0:
        lst.append(x % 10)
        x //= 10

    return True if lst == lst[::-1] else False






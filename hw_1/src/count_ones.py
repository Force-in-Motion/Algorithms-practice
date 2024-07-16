
def count_ones(n):

    if not isinstance(n, int):
        raise TypeError('Получен не верный тип данных, ожидалось целое число')

    if not n >= 0:
        raise ValueError('Передаваемое значение не может быть отрицательным')

    count = 0

    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2

    return count

count = count_ones(2478)
print(count)
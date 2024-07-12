#
# def count_ones(n):
#     if not isinstance(n, int):
#         raise TypeError('Получен не верный тип данных, ожидалось целое число')
#
#     if n < 0:
#         raise ValueError('Передаваемое значение не может быть отрицательным')
#
#     count = 0
#     while n > 0:
#         n //= 2
#         if n == 1:
#             count -= 1
#         if n % 2 != 0:
#             count += 1
#
#     return count
#
# count = count_ones(156)
# print(count)
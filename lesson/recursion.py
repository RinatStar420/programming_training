""" В упражнении вам нужно будет реализовать две взаимно рекурсивные функции (то есть использующие косвенную рекурсию):

is_odd() должна возвращать True, если число нечётное,
is_even() должна возвращать True, если число чётное.
Для простоты считаем, что аргументы всегда будут неотрицательными.

Вы, конечно, можете реализовать функции независимыми. Но задание призывает попробовать именно косвенную рекурсию!

>> is_odd(42)
False
>> is_odd(99)
True
>> is_even(42)
True
>> is_even(99)
False
"""

def is_odd(n):
    if (n == 0):
        return False
    return is_even(n - 1)


def is_even(n):
    if (n == 0):
        return True
    return is_odd(n - 1)



print(is_odd(42))
print(is_even(42))


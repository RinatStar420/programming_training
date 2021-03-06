"""
В этом упражнении вам нужно будет реализовать две функции — rotated_left() и rotated_right(). Каждая функция должна
принять список, кортеж или строку в качестве аргумента,
с помощью срезов и конкатенации получить новое значение того же типа,
вернуть это значение.
Отличаются функции лишь "направлением поворота" (см. примеры ниже).

Т.к. и строки, и списки с кортежами разрешают конкатенацию и срезы, ваш код не должен проверять тип аргумента — нужно
обойтись только лишь срезами и конкатенацией!

Обратите внимание: имена функций содержат глагол с окончанием ed — в пайтоне подобным образом часто называют
функции, возвращающие новое значение на основе старого.

При вращении влево первый элемент перемещается в конец:

#rotated_left("ABCD")
"BCDA"
При вращении вправо последний элемент перемещается в начало:

#rotated_right([1, 2, 3, 4])
[4, 1, 2, 3]
"""


def rotated_left(arg):
    if arg:
        a = arg[1::1] + arg[0:1:1]
        return a


def rotated_right(arg):
    if arg:
        a = arg[-1:] + arg[0:-1:1]
        return a



print(rotated_left("ABCD"))
print(rotated_right([1, 2, 3, 4]))

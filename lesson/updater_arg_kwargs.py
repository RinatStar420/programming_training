"""Цель данного упражнения — функция updated(). Эта функция должна принимать словарь в качестве единственного
позиционного аргумента (обязательного) и произвольное кол-во именованных аргументов. Возвращать же функция должна
новую версию словаря, в котором ключи, соответствующие именованным аргументам, должны иметь сопутствующие значения
(см.примеры).

 d = {'a': 1, 'b': False}
 updated(d, a=2, b=True, c=None)
{'a': 2, 'b': True, 'c': None}
 d
{'a': 1, 'b': False}
 updated(d) == d
True
 updated(d) is d
False"""


def updated(arg, **kwargs):
    new_arg = arg.copy()
    new_arg.update(kwargs)
    return new_arg


print(updated({'a': 1, 'b': False}, a=2, b=True, c=None))

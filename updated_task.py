import inspect
from pprint import pprint


def introspection_info(obj):
    if not isinstance(obj, (str, int)):
        obj_vars = vars(obj)
    else:
        obj_vars = []
        for i in dir(obj):
            if '__' not in i:
                obj_vars.append(i)
    dict_info = {
        'Тип объекта': type(obj),
        'Атрибуты отдельно': obj_vars,
        'Методы отдельно': inspect.getmembers(obj, predicate=inspect.isfunction),
        'Модуль, к которому объект принадлежит': inspect.getmodule(obj),
        'Имя объекта': (obj.__name__ if not isinstance(obj, (
            str, int, Food)) else f'Имена имеют только функции, классы,пакеты и так далее. Это же: {type(obj)}')
    }
    return dict_info


some_str = 'banana 25'
some_int = 256


class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste


fruit = Food('Apple', 'sweet and sour')


def homework():
    return 'Просто ф-ция для выполнения домашнего задания'


my_homework = homework
my_homework()

# pprint(introspection_info(some_str))
# pprint(introspection_info(some_int))
# pprint(introspection_info(Food))
# pprint(introspection_info(fruit))
# pprint(introspection_info(my_homework))
import inspect
from pprint import pprint


def introspection_info(obj):
    attrs = [method for method in dir(obj) if not callable(getattr(obj, method))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    dict_info = {
        'Тип объекта': type(obj),
        'Атрибуты объекта': attrs,
        'Методы объекта': methods,
        'Модуль, к которому объект принадлежит': inspect.getmodule(obj),
        'Имя объекта': (obj.__name__ if not isinstance(obj, (
            str, int, Food)) else f'Имена имеют только функции, классы,пакеты и так далее. Это: {type(obj)}')
    }
    return dict_info


some_str = 'banana 25'
some_int = 256


class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def summator(self, num_1, num_2):
        return num_1 + num_2


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

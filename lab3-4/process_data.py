import json
import sys
from cm_timer import cm_timer_1
from print_result import print_result
from unique import Unique
from random import randint

path = r"D:\documents\Basic components\lab3-4\data_light.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def f1(data):
    return list(sorted(list(iter(Unique([i.get("job-name") for i in data], ignore_case=True))), key=str.lower))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    a = [str(randint(100_000, 200_000)) for i in range(len(arg))]
    return [(", зарплата ").join(i) for i in zip(arg, a)]


if __name__ == '__main__':
    with cm_timer_1():
            f4(f3(f2(f1(data))))

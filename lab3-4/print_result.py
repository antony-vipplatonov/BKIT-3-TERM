# 5
def print_result(func):
    def result(*arg):
        a = func(*arg)
        if isinstance(a, list):
            print(func.__name__, *a, sep="\n")
        elif isinstance(a, dict):
            print(func.__name__, *[f"{key} = {val}" for key, val in a.items()], sep="\n")
        else:
            print(func.__name__, a, sep="\n")
        return a

    return result


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

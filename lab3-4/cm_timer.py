# 6
import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            b = time.time() - self.start
            print(f"time: {b}")


@contextmanager
def cm_timer_2():
    start = time.time()
    yield 1
    b = time.time() - start
    print(f"time: {b}")


'''
with cm_timer_1():
    for i in range(100000):
        pass
with cm_timer_2():
    for i in range(1000000):
        pass
'''

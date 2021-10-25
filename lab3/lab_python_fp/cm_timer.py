import time
from contextlib import contextmanager


class cm_timer_1:       #Таймер на основе класса
    
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(cm_timer_1.__name__, time.time() - self.start_time)


@contextmanager
def cm_timer_2():       #Таймер на основе готовой библиотеки
    start_time = time.time()
    yield
    print(cm_timer_2.__name__, time.time() - start_time)


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)

import time
from threading import Thread

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ['a', 'b', 'c', 'd', 'i', 'f', 'g', 'j']


def func():
    for i in numb:
        time.sleep(1)
        print(i)


def func_1():
    for i in text:
        time.sleep(1)
        print(i)


the_first = Thread(target=func)
the_second = Thread(target=func_1)

the_first.start()
the_second.start()

the_first.join()
the_second.join()

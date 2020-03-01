# https://leetcode.com/problems/print-in-order/

class Foo:
    def __init__(self):
        self.order = [1, 2, 3]

    def first(self, printFirst) -> None:
        printFirst()
        self.order.pop(0)

    def second(self, printSecond) -> None:
        while self.order[0] != 2:
            pass
        printSecond()
        self.order.pop(0)

    def third(self, printThird) -> None:
        while self.order[0] != 3:
            pass
        printThird()
        self.order = [1, 2, 3]


import threading

a = Foo()


def printer(name):
    def innner():
        print(f'{name}', end='')

    return innner


t3 = threading.Thread(target=a.first, args=(printer('third'),))
t2 = threading.Thread(target=a.first, args=(printer('second '),))
t1 = threading.Thread(target=a.first, args=(printer('first '),))

t1.start()
t2.start()
t3.start()

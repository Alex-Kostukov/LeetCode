# https://leetcode.com/problems/print-foobar-alternately/
from threading import Lock, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo) -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar) -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


def print_foo():
    print('foo', end='')


def print_bar():
    print('bar', end='')


a = FooBar(10)

t1 = Thread(target=a.foo, args=(print_foo,))
t2 = Thread(target=a.bar, args=(print_bar,))
t1.start()
t2.start()

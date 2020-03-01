# https://leetcode.com/problems/print-zero-even-odd/
from threading import Lock, Thread

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_zero = Lock()
        self.lock_even = Lock()
        self.lock_odd = Lock()
        self.lock_even.acquire()
        self.lock_odd.acquire()

    def zero(self, printNumber) -> None:
        for i in range(1, self.n + 1):
            self.lock_zero.acquire()
            printNumber(0)

            if i % 2 == 0:
                self.lock_even.release()
            else:
                self.lock_odd.release()

    def even(self, printNumber) -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.lock_even.acquire()
                printNumber(i)
                self.lock_zero.release()

    def odd(self, printNumber) -> None:
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.lock_odd.acquire()
                printNumber(i)
                self.lock_zero.release()


def printer(n):
    print(n, end='')


a = ZeroEvenOdd(9)
t1 = Thread(target=a.zero, args=(printer,))
t2 = Thread(target=a.even, args=(printer,))
t3 = Thread(target=a.odd, args=(printer,))

t1.start()
t2.start()
t3.start()

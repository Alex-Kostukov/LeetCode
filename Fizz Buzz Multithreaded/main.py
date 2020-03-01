# https://leetcode.com/problems/fizz-buzz-multithreaded/
from threading import Lock, Thread


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_lock = Lock()
        self.buzz_lock = Lock()
        self.fizzbuzz_lock = Lock()
        self.number_lock = Lock()

        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fizzbuzz_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz) -> None:
        for i in range(3, self.n + 1, 3):

            if not (i % 3 == 0 and i % 5 == 0):
                self.fizz_lock.acquire()
                printFizz()
                self.number_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz) -> None:
        for i in range(5, self.n + 1, 5):
            if not (i % 3 == 0 and i % 5 == 0):
                self.buzz_lock.acquire()
                printBuzz()
                self.number_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz) -> None:
        for i in range(15, self.n + 1, 15):
            self.fizzbuzz_lock.acquire()
            printFizzBuzz()
            self.number_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber) -> None:
        self.number_lock.acquire()
        for i in range(1, self.n + 1):

            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzz_lock.release()
            elif i % 3 == 0:
                self.fizz_lock.release()
            elif i % 5 == 0:
                self.buzz_lock.release()

            else:
                printNumber(i)
                self.number_lock.release()

            self.number_lock.acquire()


def printer(what):
    def _printer(n=None):
        if not n:
            print(what, end=' ')
        else:
            print(n, end=' ')

    return _printer


a = FizzBuzz(60)

t1 = Thread(target=a.fizz, args=(printer('fizz'),))
t2 = Thread(target=a.buzz, args=(printer('buzz'),))
t3 = Thread(target=a.fizzbuzz, args=(printer('fizzbuzz'),))
t4 = Thread(target=a.number, args=(printer(''),))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join(timeout=0.5)
t2.join(timeout=0.5)
t3.join(timeout=0.3)
t4.join(timeout=0.3)
print()
print(t1.is_alive())
print(t2.is_alive())
print(t3.is_alive())
print(t4.is_alive())

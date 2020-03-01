# https://leetcode.com/problems/building-h2o/
from threading import Semaphore, Thread


class H2O:
    def __init__(self):
        self.h_lock = Semaphore()
        self.o_lock = Semaphore()
        self.time_to_release = False

    def hydrogen(self, releaseHydrogen) -> None:
        self.h_lock.acquire()
        releaseHydrogen()
        if self.time_to_release:
            self.o_lock.release()  # 2 H's got, awaiting O

        self.time_to_release ^= True

    def oxygen(self, releaseOxygen) -> None:
        self.o_lock.acquire()
        releaseOxygen()
        self.h_lock.release()  # awaiting +1 H
        self.h_lock.release()  # awaiting +1 H


def printer(what):
    def _printer():
        print(what, end='')

    return _printer


a = H2O()
Thread(target=a.oxygen, args=(printer('O'),)).start()
Thread(target=a.oxygen, args=(printer('O'),)).start()
Thread(target=a.hydrogen, args=(printer('H'),)).start()
Thread(target=a.hydrogen, args=(printer('H'),)).start()
Thread(target=a.hydrogen, args=(printer('H'),)).start()
Thread(target=a.hydrogen, args=(printer('H'),)).start()
Thread(target=a.hydrogen, args=(printer('H'),)).start()

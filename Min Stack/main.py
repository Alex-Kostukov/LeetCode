from collections import deque

from bisect import insort_left


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_list = []

    def push(self, x: int) -> None:
        insort_left(self.min_list, x)
        self.stack.appendleft(x)

    def pop(self) -> None:
        value = self.stack.popleft()
        self.min_list.remove(value)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_list[0]


# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.keys = set()

    def add(self, key: int) -> None:
        self.keys.add(key)

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.keys.remove(key)

    def contains(self, key: int) -> bool:
        return self.keys.__contains__(key)

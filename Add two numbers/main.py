# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def to_int(self, l: ListNode):
        if l.next:
            return self.to_int(l.next) + str(l.val)
        return str(l.val)

    def to_linked_list(self, num: str):
        current = None
        first = None
        for digit in reversed(num):
            if current:
                current.next = ListNode(int(digit))
                current = current.next
            else:
                current = ListNode(int(digit))
                first = current
        return first

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = int(self.to_int(l1))
        b = int(self.to_int(l2))
        c = a + b
        return self.to_linked_list(str(c))

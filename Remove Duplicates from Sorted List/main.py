class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        None is not the sorted linked list, LeetCode!!!
        """

        first = current = head

        if head is None:
            return None

        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return first

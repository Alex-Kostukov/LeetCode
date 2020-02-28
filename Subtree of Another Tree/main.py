# https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def checker(f):
            def _checker(s, t):
                if s is t is None:
                    return True

                if s is None or t is None:
                    return False

                return f(s, t)

            return _checker

        @checker
        def go_deep(s, t):

            if s.val == t.val and check(s, t):
                return True

            return go_deep(s.left, t) or go_deep(s.right, t)

        @checker
        def check(s, t):

            if s.val != t.val:
                return False

            return check(s.left, t.left) and check(s.right, t.right)

        return go_deep(s, t)

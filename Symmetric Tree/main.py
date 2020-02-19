# https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or root.right is root.left is None:
            return True

        def _is_symmetric(node1, node2):
            if node1 is node2 is None:
                return True

            if node1 and node2 and node1.val == node2.val:
                return _is_symmetric(node1.left, node2.right) and _is_symmetric(node1.right, node2.left)
            else:
                return False

        return _is_symmetric(root.left, root.right)

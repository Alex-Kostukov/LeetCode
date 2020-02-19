# https://leetcode.com/problems/binary-tree-tilt/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node {self.val}'


"""
[1,2,3,4,null,5]

        1
      2   3
    4    5

Tilt of ith node equal = |sum of left node values - sum of right node values|
Tree tilt defined as sum of all nodes tilt


[1,2,null,3,4]
        1
      2  
    3  4
    
0 + 0 + 1     
"""


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0

        tree_tilt = 0

        def _sum(node) -> (int, int):  # (sum of all down node values + current node value)
            nonlocal tree_tilt
            if node is None:
                return 0

            left = _sum(node.left)
            right = _sum(node.right)
            tree_tilt += abs(left - right)

            return node.val + left + right

        _sum(root)
        return abs(tree_tilt)


"""
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
"""

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
print(Solution().findTilt(root))

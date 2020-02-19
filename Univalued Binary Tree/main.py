class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def check_deeper(node):
            if node.val != root.val:
                return False

            result = True
            if node.left:
                result = result and check_deeper(node.left)

            if node.right:
                result = result and check_deeper(node.right)

            return result

        return check_deeper(root)

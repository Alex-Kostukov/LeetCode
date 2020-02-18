class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node: {self.val}'


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if not nums:
            return None

        def get_BST(nums):
            mid = len(nums) // 2
            if not nums:
                return None

            node = TreeNode(nums[mid])

            if len(nums) == 1:
                return node
            else:
                node.left = get_BST(nums[:mid])
                node.right = get_BST(nums[mid + 1:])
                return node


        return get_BST(nums)

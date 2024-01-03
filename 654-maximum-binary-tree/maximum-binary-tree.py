# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def dfs(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            maxi = -inf
            idx = -1
            for i, n in enumerate(arr):
                if n > maxi:
                    maxi = n
                    idx = i
            node = TreeNode(maxi)
            node.left = dfs(arr[:idx])
            node.right = dfs(arr[idx+1:])
            return node
        return dfs(nums)
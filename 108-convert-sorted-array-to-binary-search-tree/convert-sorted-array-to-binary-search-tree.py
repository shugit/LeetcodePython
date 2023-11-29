# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r:
                return None
            mid = l + (r-l) // 2
            curr = TreeNode(nums[mid])
            curr.left = build(l, mid - 1)
            curr.right = build(mid + 1, r) 
            return curr
        return build(0, len(nums)-1)
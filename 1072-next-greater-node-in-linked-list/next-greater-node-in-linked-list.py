# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        stack = []
        res = []
        i = 0
        while node:
            res.append(0)
            while stack and stack[-1][1] < node.val:
                prev_i, prev = stack.pop()
                res[prev_i] = node.val
            stack.append([i, node.val])
            node = node.next
            i += 1
        return res
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head
        while r and r.next:
            r = r.next.next
            l = l.next
            if l == r:
                break
        if not r or not r.next:
            return None
        l = head
        while l != r:
            l, r = l.next, r.next
        return l
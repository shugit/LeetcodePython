# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        q = []
        cur = head
        while cur:
            q.append([cur.val, cur])
            cur = cur.next
        q.sort(key=lambda x: x[0])
        for i in range(1, len(q)):
            q[i-1][1].next = q[i][1]
        q[len(q)-1][1].next = None
        return q[0][1]
        
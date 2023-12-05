# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
      def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
          return head
        tail = head
        n = 1
        while tail.next:
          tail = tail.next
          n += 1
        tail.next = head
        l = head
        r = head
        for i in range(0, n - k % n - 1):
          r = r.next
        new_head = r.next
        # print(l.val, r.val, new_head.val, n)
        r.next = None
        return new_head



    

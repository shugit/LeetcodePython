# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        head, tail = head, head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
        def reverseList(head, k):
            if not head or not head.next or k == 1:
                return head
            p = reverseList(head.next, k-1)
            head.next.next = head
            head.next = None
            return p
        newHead = reverseList(head, k)
        head.next = self.reverseKGroup(tail,k)
        return newHead
        
       
            
            
            
        
        
        
        
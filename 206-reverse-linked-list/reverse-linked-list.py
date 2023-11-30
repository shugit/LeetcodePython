# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rever(head)
        # return self.iter(head)

    def rever(self,head):
        if not head or not head.next:
            return head
        p = self.rever(head.next)
        head.next.next = head
        head.next = None
        return p


    def iter(self,head):
        prev,curr = None,head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
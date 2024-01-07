class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        successor = None
        def reverseN(head, m):
            if not head.next:
                return head
            nonlocal successor
            if m == 1:
                successor = head.next
                return head
            last = reverseN(head.next, m - 1)
            head.next.next = head
            head.next = successor
            return last

        if left == 1:
            return reverseN(head, right)
        else:
            head.next =  self.reverseBetween(head.next, left-1, right-1)
            return head

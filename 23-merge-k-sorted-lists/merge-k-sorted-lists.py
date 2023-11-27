# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge2(self, l1,l2):
        dummy = ListNode(0)
        curr = dummy
        p1,p2 = l1,l2
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        while p1:
            curr.next = p1
            curr = curr.next
            p1 = p1.next
        while p2:
            curr.next = p2
            curr = curr.next
            p2 = p2.next
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            dummy = ListNode(-1)
            curr = dummy
            p1 = l1
            p2 = l2
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    curr = curr.next
                    p1 = p1.next
                else:
                    curr.next = p2
                    curr = curr.next
                    p2 = p2.next
            while p1:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            while p2:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
            return dummy.next
        
        if not lists:
            return None
        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            merged_list = self.merge2(l1,l2)
            lists.append(merged_list)
        return lists[0]

        
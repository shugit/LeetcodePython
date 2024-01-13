# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.heapSol(lists)

    def heapSol(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda n1, n2: n1.val < n2.val
        dummy = ListNode(-1)
        p = dummy
        q = []
        for head in lists:
            if head:
                heapq.heappush(q, (head.val, head))
        while q:
            node = heapq.heappop(q)[1]
            p.next = node
            if node.next:
                heapq.heappush(q, (node.next.val, node.next))
            p = p.next
        return dummy.next
    
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
        
    def mergeSortSol(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        arr = deque(lists)
        while len(arr)> 1:
            l1 = arr.popleft()
            l2 = arr.popleft()
            merged_list = self.merge2(l1,l2)
            arr.append(merged_list)
        return arr[0]

        
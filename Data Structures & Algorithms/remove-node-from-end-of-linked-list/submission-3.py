# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        l = head
        curr = n
        while r and curr > 0:
            curr-=1
            r = r.next
        if r is None:
            return head.next
        while r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return head
        
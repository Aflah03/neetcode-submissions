# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return 
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        list2= prev
        list1 = head
        dummy = res  = ListNode()
        while list1 and list2:
            res.next = list1
            list1 = list1.next
            res = res.next
            res.next = list2
            list2 = list2.next
            res = res.next
        res.next = list1 or list2 or None
        head = dummy.next
        

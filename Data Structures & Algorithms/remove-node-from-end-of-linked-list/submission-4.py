# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = n
        temp = head
        while k >  0 and temp:
            temp = temp.next
            k-=1
        if temp is None:
            return head.next
        temp1 = head
        while temp.next:
            temp = temp.next
            temp1 = temp1.next
        temp1.next = temp1.next.next
        return head
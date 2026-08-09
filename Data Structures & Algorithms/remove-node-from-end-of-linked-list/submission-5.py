# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        temp = head
        while temp:
            temp = temp.next
            k+=1
        if k==n:
            return head.next
        curr = k-n-1
        temp = head
    
        while curr:
            curr-=1
            temp = temp.next
        temp.next = temp.next.next
        return head
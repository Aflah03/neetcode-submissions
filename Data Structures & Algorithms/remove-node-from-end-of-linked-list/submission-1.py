# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        temp  =head
        while temp:
            N+=1
            temp = temp.next
        if N == n:
            return head.next
        curr = N-(n+1)

        temp =head
        while curr:
           temp = temp.next
           curr-=1
        nxt = temp.next
        temp.next = nxt.next
        del nxt
        return head